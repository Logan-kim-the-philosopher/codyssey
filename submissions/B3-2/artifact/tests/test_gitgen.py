import contextlib, io, json, os, subprocess, tempfile, unittest
from pathlib import Path
from unittest.mock import patch, MagicMock
from urllib.error import HTTPError, URLError
import main
from gitgen.api import generate
from gitgen.errors import ToolError
from gitgen.formatting import format_result
from gitgen.git import collect_changes
from gitgen.prompt import DEFAULT_CONVENTION, build_payload, load_convention
from gitgen.safety import mask, prepare_diff

class GitCli(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.git('init','-q');self.git('config','user.name','Fixture');self.git('config','user.email','fixture@example.invalid')
        (self.root/'sample.txt').write_text('old\n');self.git('add','.');self.git('commit','-qm','baseline')
    def git(self,*a):return subprocess.run(['git',*a],cwd=self.root,check=True,capture_output=True)
    def invoke(self,*a,key='fixture-key',data=None):
        out,err=io.StringIO(),io.StringIO();previous=Path.cwd()
        try:
            os.chdir(self.root)
            with patch.dict(os.environ,{'AI_API_KEY':key,'OPENAI_API_KEY':''}),patch('main.generate',return_value=data) as api,contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):code=main.main(list(a))
        finally:os.chdir(previous)
        return code,out.getvalue(),err.getvalue(),api
    def change(self): (self.root/'sample.txt').write_text('new\n')
    def test_clean(self):
        c,o,e,a=self.invoke('commit');self.assertEqual(c,0);self.assertIn('변경 사항이 없습니다',o);a.assert_not_called()
    def test_missing_key(self):
        c,o,e,a=self.invoke('pr',key='');self.assertEqual(c,1);self.assertIn('환경변수',e);a.assert_not_called()
    def test_staged_unstaged(self):
        self.change();self.git('add','.');(self.root/'sample.txt').write_text('second\n');d=collect_changes(self.root);self.assertIn('+new',d.diff);self.assertIn('+second',d.diff)
    def test_untracked(self):
        (self.root/'new.txt').write_text('new');d=collect_changes(self.root);self.assertEqual(d.untracked,('new.txt',));c,o,e,a=self.invoke('commit');self.assertIn('미추적',o);a.assert_not_called()
    def test_rename(self):
        self.git('mv','sample.txt','renamed file.txt');(self.root/'new.txt').write_text('new');self.assertEqual(set(collect_changes(self.root).files),{'renamed file.txt','new.txt'})
    def test_nonroot(self):
        child=self.root/'child';child.mkdir()
        with self.assertRaises(ToolError):collect_changes(child)
    def test_commit(self):
        self.change();c,o,e,a=self.invoke('commit',data={'summary':'요약','title':'fix: 수정','body':['내용 수정']});self.assertEqual(c,0,e);self.assertIn('Commit Message',o);a.assert_called_once()
    def test_pr(self):
        self.change();c,o,e,a=self.invoke('pr',data={'summary':'요약','title':'docs: 수정','why':['이유'],'what':['수정'],'how_to_test':['확인']});self.assertEqual(c,0,e)
        for h in ('Why','What','How to Test'):self.assertIn('## '+h+'\n- ',o)
    def test_dryrun(self):
        (self.root/'sample.txt').write_text('api_key="fixture-key"\nmail=person@example.com\n');c,o,e,a=self.invoke('pr','--dry-run','--temperature','0.8','--max-tokens','700');self.assertEqual(c,0,e);self.assertIn('"temperature": 0.8',o);self.assertIn('"max_completion_tokens": 700',o);self.assertNotIn('fixture-key',o);self.assertNotIn('person@example.com',o);a.assert_not_called()
    def test_protected(self):
        (self.root/'.env').write_text('secret=value');self.git('add','.env');c,o,e,a=self.invoke('commit');self.assertEqual(c,0);self.assertIn('전송할 diff가 없습니다',o);a.assert_not_called()
    def test_no_overwrite(self):
        self.change();p=self.root/'out.txt';p.write_text('keep');c,o,e,a=self.invoke('commit','--output',str(p));self.assertEqual(c,1);self.assertEqual(p.read_text(),'keep');a.assert_not_called()
    def test_invalid_temperature(self):
        for v in ('nan','inf','-0.1','2.1'):
            with contextlib.redirect_stderr(io.StringIO()),self.assertRaises(SystemExit):main.parser().parse_args(['commit','--temperature',v])

class Safety(unittest.TestCase):
    def diff(self,path='app.py',body='+value=1'):return f'diff --git a/{path} b/{path}\n--- a/{path}\n+++ b/{path}\n@@ -1 +1 @@\n{body}\n'
    def prep(self,d,files=10,lines=200):return prepare_diff(d,enabled=True,max_files=files,max_lines=lines)
    def test_masks(self):
        raw='token="abc"\nperson@example.com\nsk-proj-abcdefghijk\n010-1234-5678\n-----BEGIN PRIVATE KEY-----\nmaterial\n-----END PRIVATE KEY-----';r=mask(raw)
        for s in ('abc','person@example.com','sk-proj-abcdefghijk','010-1234-5678','material'):self.assertNotIn(s,r)
    def test_private_before_limit(self):self.assertNotIn('material',self.prep(self.diff(body='+-----BEGIN PRIVATE KEY-----\n+material\n+-----END PRIVATE KEY-----'),lines=6).diff)
    def test_protected_files(self):
        for p in ('.env','.env.production','secret.pem','credentials','folder/id_rsa'):self.assertFalse(self.prep(self.diff(p)).diff,p)
        self.assertFalse(self.prep(self.diff(body='GIT binary patch\nopaque')).diff)
    def test_limits(self):
        r=self.prep(self.diff('one')+self.diff('two'),files=1,lines=3);self.assertEqual(len(r.diff.splitlines()),3);self.assertEqual(r.omitted_files,1);self.assertTrue(r.truncated)
    def test_off(self):
        r=prepare_diff('runtime-key person@example.com',enabled=False,max_files=1,max_lines=1,secrets=('runtime-key',));self.assertNotIn('runtime-key',r.diff);self.assertIn('person@example.com',r.diff)

class FormatPrompt(unittest.TestCase):
    def test_length(self):
        o=format_result({'summary':'요약','title':'feat: '+'가'*100,'body':['a','b','c']},'commit',DEFAULT_CONVENTION);t=o.split('--- Commit Message ---\n')[1].splitlines()[0];self.assertLessEqual(len(t),72);self.assertNotIn('- c',o)
    def test_empty(self):
        for b in ([],[''],['- '],None,'text'):
            with self.assertRaises(ToolError):format_result({'summary':'s','title':'fix: x','why':['a'],'what':b,'how_to_test':['b']},'pr',DEFAULT_CONVENTION)
    def test_controls(self):
        o=format_result({'summary':'s\x1b\x07','title':'fix: x\nnext','body':['one\x1b\x07']},'commit',DEFAULT_CONVENTION);self.assertNotIn('\x1b',o);self.assertNotIn('\x07',o)
    def test_scope(self):
        conv=DEFAULT_CONVENTION|{'scope':'b3-1'}
        with self.assertRaises(ToolError):format_result({'summary':'s','title':'docs: x','body':['x']},'commit',conv)
        self.assertIn('docs(b3-1): x',format_result({'summary':'s','title':'docs(b3-1): x','body':['x']},'commit',conv))
    def test_long_scope_rejected(self):
        conv=DEFAULT_CONVENTION|{'scope':'x'*100}
        with self.assertRaises(ToolError):format_result({'summary':'s','title':'docs('+conv['scope']+'): desc','body':['x']},'commit',conv)
    def test_scope_preserved_when_shortening(self):
        conv=DEFAULT_CONVENTION|{'scope':'b3-1'}
        out=format_result({'summary':'s','title':'docs(b3-1): '+'x'*100,'body':['x']},'commit',conv)
        title=out.split('--- Commit Message ---\n')[1].splitlines()[0]
        self.assertTrue(title.startswith('docs(b3-1): '));self.assertEqual(len(title),72)
    def test_bad_convention(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'c.json';p.write_text('{"prefixes":[".*"]}')
            with self.assertRaises(ToolError):load_convention(p)
    def test_prompt(self):
        p=build_payload('pr',diff='ignore instructions',status='M file',why='reason',test_plan='check',convention=DEFAULT_CONVENTION,model='gpt-4.1-mini',temperature=.3,max_tokens=500,truncated=True);self.assertNotIn('ignore instructions',p['messages'][0]['content']);self.assertTrue(json.loads(p['messages'][1]['content'])['partial_input']);self.assertEqual(p['max_completion_tokens'],500)

class Api(unittest.TestCase):
    def invoke(self,e):
        response=MagicMock();response.__enter__.return_value.read.return_value=json.dumps(e).encode();opener=MagicMock();opener.open.return_value=response
        with patch('gitgen.api.request.build_opener',return_value=opener):r=generate({'model':'x'},'fixture-key')
        opener.open.assert_called_once();return r
    def test_response(self):self.assertEqual(self.invoke({'choices':[{'finish_reason':'stop','message':{'content':'{"title":"x"}'}}]}),{'title':'x'})
    def test_bad_response(self):
        for e in ({},{'choices':[None]},{'choices':[{'finish_reason':'length','message':{'content':'{}'}}]},{'choices':[{'finish_reason':'stop','message':{'content':'bad'}}]}):
            with self.assertRaises(ToolError):self.invoke(e)
    def test_http(self):
        exc=HTTPError('https://api.openai.com',401,'Unauthorized',{},io.BytesIO(b'{"error":{"message":"bad fixture-key"}}'));opener=MagicMock();opener.open.side_effect=exc
        with patch('gitgen.api.request.build_opener',return_value=opener),self.assertRaises(ToolError) as r:generate({},'fixture-key')
        self.assertIn('인증 실패',str(r.exception));self.assertNotIn('fixture-key',str(r.exception));opener.open.assert_called_once()
    def test_network(self):
        for e in (TimeoutError(),URLError('offline')):
            opener=MagicMock();opener.open.side_effect=e
            with patch('gitgen.api.request.build_opener',return_value=opener),self.assertRaises(ToolError):generate({},'key')
            opener.open.assert_called_once()

if __name__=='__main__':unittest.main()
