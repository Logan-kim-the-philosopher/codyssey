import importlib.util
import io
import os
from pathlib import Path
import unittest
from unittest.mock import patch
from gitgen.environment import public_environment
from gitgen.git import collect_changes
import test_gitgen

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('bws_entry', ROOT/'tools/bws_entry.py')
entry = importlib.util.module_from_spec(spec);spec.loader.exec_module(entry)

spec_run=importlib.util.spec_from_file_location('bws_run', ROOT/'tools/bws_run.py')
launcher=importlib.util.module_from_spec(spec_run);spec_run.loader.exec_module(launcher)

class Writer(io.StringIO):
    def close(self):pass

class BwsTests(unittest.TestCase):
    def test_timeout_kills_process_group(self):
        from unittest.mock import MagicMock
        import signal
        process=MagicMock();process.pid=12345
        with patch.object(launcher.os,'killpg') as kill:
            launcher.stop_tree(process)
        kill.assert_called_once_with(12345,signal.SIGKILL)
        process.wait.assert_called_once()
    def test_launch_failure_closes_pipe(self):
        import contextlib
        from unittest.mock import MagicMock
        read_fd,write_fd=os.pipe()
        keychain=MagicMock(returncode=0,stdout=b'fake-bws-access-token')
        with patch.object(launcher.subprocess,'run',return_value=keychain),patch.object(launcher.subprocess,'Popen',side_effect=OSError('unavailable')),patch.object(launcher.os,'pipe',return_value=(read_fd,write_fd)),contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(launcher.main(['commit']),4)
        for fd in (read_fd,write_fd):
            with self.assertRaises(OSError):os.fstat(fd)
    def test_gateway_payload_idempotent(self):
        from gitgen.api import prepare_payload
        first=prepare_payload({'max_completion_tokens':800,'store':False},'https://copa.codyssey.kr/v1')
        self.assertEqual(prepare_payload(first,'https://copa.codyssey.kr/v1'),first)
    def test_gateway_compatibility_payload(self):
        from gitgen.api import generate
        from unittest.mock import MagicMock
        import json
        response=MagicMock();response.__enter__.return_value.read.return_value=b'{"choices":[{"finish_reason":"stop","message":{"content":"{}"}}]}'
        opener=MagicMock();opener.open.return_value=response
        payload={'model':'gpt-5.4-mini','messages':[],'max_completion_tokens':800,'temperature':1,'store':False,'response_format':{'type':'json_object'}}
        with patch('gitgen.api.request.build_opener',return_value=opener):generate(payload,'fake-llm-secret',base_url='https://copa.codyssey.kr/v1')
        req=opener.open.call_args.args[0];sent=json.loads(req.data)
        self.assertEqual(req.full_url,'https://copa.codyssey.kr/v1/chat/completions')
        self.assertEqual(sent['max_tokens'],800)
        self.assertNotIn('store',sent);self.assertNotIn('response_format',sent)
        self.assertNotIn('fake-llm-secret',req.data.decode())
        self.assertEqual(payload['max_completion_tokens'],800)
    def test_unapproved_endpoint(self):
        from gitgen.api import endpoint_for
        from gitgen.errors import ToolError
        for url in ('http://copa.codyssey.kr/v1','https://evil.invalid/v1','https://copa.codyssey.kr/v1?key=fake','https://user:password@copa.codyssey.kr/v1'):
            with self.assertRaises(ToolError):endpoint_for(url)
        self.assertEqual(endpoint_for('https://copa.codyssey.kr/v1'),'https://copa.codyssey.kr/v1/chat/completions')
    def test_error_body_never_echoed(self):
        from gitgen.api import generate
        from gitgen.errors import ToolError
        from urllib.error import HTTPError
        from unittest.mock import MagicMock
        body=io.BytesIO(b'{"error":{"message":"bad sk-fake-********suffix, temperature unsupported","param":"temperature"}}');exc=HTTPError('https://copa.codyssey.kr',401,'Authentication',{},body)
        opener=MagicMock();opener.open.side_effect=exc
        with patch('gitgen.api.request.build_opener',return_value=opener),self.assertRaises(ToolError) as caught:generate({},'fake-llm-secret',base_url='https://copa.codyssey.kr/v1')
        self.assertNotIn('suffix',str(caught.exception))
        self.assertNotIn('sk-fake',str(caught.exception))
        self.assertIn('temperature',str(caught.exception))
        self.assertNotIn('fake-llm-secret',str(caught.exception))
    def test_environment_allowlist(self):
        result=public_environment({'PATH':'/usr/bin','AI_API_KEY':'fake-llm-secret','BWS_ACCESS_TOKEN':'fake-bws-secret','CODEYSSEY_LLM_API':'fake-llm-secret','OTHER_SECRET':'fake-other-secret','LANG':'C'})
        self.assertEqual(set(result),{'PATH','LANG'})
    def test_bridge_alias_and_removal(self):
        writer=Writer();seen={}
        def fake(argv):
            seen.update(os.environ)
            print('[DONE] safe generated output')
            return 0
        with patch.dict(os.environ,{'CODEYSSEY_LLM_API':'fake-llm-secret','BWS_ACCESS_TOKEN':'fake-bws-secret','OTHER_SECRET':'fake-other-secret'},clear=True),patch('main.main',side_effect=fake),patch.object(entry.os,'fdopen',return_value=writer):
            code=entry.consume(['commit'])
            self.assertNotIn('AI_API_KEY',os.environ)
        self.assertEqual(code,0)
        self.assertEqual(seen['AI_API_KEY'],'fake-llm-secret')
        self.assertNotIn('BWS_ACCESS_TOKEN',seen)
        self.assertNotIn('OTHER_SECRET',seen)
        self.assertNotIn('CODEYSSEY_LLM_API',seen)
        self.assertNotIn('fake-llm-secret',writer.getvalue())
    def test_secret_output_discarded(self):
        def leaking(argv):print(os.environ['AI_API_KEY']);return 0
        with patch.dict(os.environ,{'CODEYSSEY_LLM_API':'fake-llm-secret'},clear=True),patch('main.main',side_effect=leaking),patch.object(entry.os,'fdopen') as fd:
            self.assertEqual(entry.consume(['commit']),5)
            fd.assert_not_called()
    def test_missing_bws_secret(self):
        with patch.dict(os.environ,{},clear=True):self.assertEqual(entry.consume(['commit']),3)
    def test_exception_not_printed(self):
        with patch.dict(os.environ,{'CODEYSSEY_LLM_API':'fake-llm-secret'},clear=True),patch('main.main',side_effect=RuntimeError('fake-llm-secret')),patch.object(entry.os,'fdopen') as fd:
            self.assertEqual(entry.consume(['commit']),4);fd.assert_not_called()

class GitSecretTests(unittest.TestCase):
    setUp = test_gitgen.GitCli.setUp
    git = test_gitgen.GitCli.git
    def test_git_does_not_inherit_secret(self):
        import gitgen.git as module
        original=module.subprocess.run
        seen=[]
        def spy(*a,**kw):seen.append(kw['env']);return original(*a,**kw)
        with patch.dict(os.environ,{'AI_API_KEY':'fake-llm-secret','BWS_ACCESS_TOKEN':'fake-bws-secret'}),patch.object(module.subprocess,'run',side_effect=spy):collect_changes(self.root)
        self.assertEqual(len(seen),3)
        for env in seen:
            self.assertNotIn('AI_API_KEY',env);self.assertNotIn('BWS_ACCESS_TOKEN',env)

if __name__=='__main__':unittest.main()
