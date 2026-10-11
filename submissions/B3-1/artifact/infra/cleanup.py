"""Remove only IDs recorded for this B3-1 lab; no discovery-based deletion."""
import json, os, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/'evidence/resources.json').read_text())
AWS='/Users/hskim/.local/bin/aws'
def call(*args,env=None,profile=True):
 cmd=[AWS,*args,'--region',state['region'],'--output','json']
 if profile: cmd+=['--profile','codyssey']
 return json.loads(subprocess.check_output(cmd,env=env,text=True) or '{}')
c=call('sts','assume-role','--role-arn','arn:aws:iam::888782968605:role/codyssey-b3-1-deployer','--role-session-name','B3-1-cleanup')['Credentials']
env=dict(os.environ,AWS_ACCESS_KEY_ID=c['AccessKeyId'],AWS_SECRET_ACCESS_KEY=c['SecretAccessKey'],AWS_SESSION_TOKEN=c['SessionToken'])
def aws(*args): return call(*args,env=env,profile=False)
result=[]
def remove(action,*args):
 aws('ec2',action,*args); result.append({'action':action,'args':args,'result':'success'})
 (ROOT/'evidence/cleanup-result.json').write_text(json.dumps(result,indent=2)+'\n')
# Check the tag before terminating the recorded instance.
instance=aws('ec2','describe-instances','--instance-ids',state['instance'])['Reservations'][0]['Instances'][0]
assert {'Key':'Assignment','Value':'B3-1'} in instance.get('Tags',[])
remove('terminate-instances','--instance-ids',state['instance'])
aws('ec2','wait','instance-terminated','--instance-ids',state['instance'])
remove('delete-security-group','--group-id',state['securityGroup'])
remove('delete-key-pair','--key-name',state['keyPair'])
remove('disassociate-route-table','--association-id',state['routeAssociation'])
remove('delete-subnet','--subnet-id',state['subnet'])
remove('delete-route-table','--route-table-id',state['routeTable'])
remove('detach-internet-gateway','--internet-gateway-id',state['igw'],'--vpc-id',state['vpc'])
remove('delete-internet-gateway','--internet-gateway-id',state['igw'])
remove('delete-vpc','--vpc-id',state['vpc'])
print('Recorded network and instance removed. Verify EBS/address inventory and then remove the lab IAM role.')
