"""Create one tagged B3-1 lab; save each ID immediately for later cleanup."""
import json, os, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
JOURNAL = ROOT / 'evidence/resources.json'
if JOURNAL.exists():
    raise SystemExit('Resource journal exists; inspect it before any new provisioning.')
REGION = 'ap-southeast-2'
AWS = '/Users/hskim/.local/bin/aws'
def call(*args, env=None, profile=True):
    cmd = [AWS, *args, '--region', REGION, '--output', 'json']
    if profile:
        cmd += ['--profile', 'codyssey']
    return json.loads(subprocess.check_output(cmd, env=env, text=True) or '{}')
credentials = call('sts','assume-role','--role-arn','arn:aws:iam::888782968605:role/codyssey-b3-1-deployer','--role-session-name','B3-1-lab')['Credentials']
env = dict(os.environ, AWS_ACCESS_KEY_ID=credentials['AccessKeyId'], AWS_SECRET_ACCESS_KEY=credentials['SecretAccessKey'], AWS_SESSION_TOKEN=credentials['SessionToken'])
def aws(*args):
    return call(*args, env=env, profile=False)
state = {'region': REGION, 'project': 'cdsy', 'role': 'codyssey-b3-1-deployer'}
def save(key, value):
    state[key] = value
    JOURNAL.write_text(json.dumps(state, indent=2)+'\n')
    print(key, value, flush=True)
def tag(resource):
    aws('ec2','create-tags','--resources',resource,'--tags','Key=Assignment,Value=B3-1','Key=Name,Value=codyssey-b3-1')
# Determine the SSH source externally without disclosing any credentials.
ip = subprocess.check_output(['curl','--fail','--silent','https://checkip.amazonaws.com'],text=True).strip()
import ipaddress
ipaddress.IPv4Address(ip)
save('sshCidr',ip+'/32')
key = Path('/private/tmp/codyssey-b3-1-key')
if not key.exists():
    subprocess.run(['ssh-keygen','-q','-t','ed25519','-N','','-f',str(key)],check=True)
aws('ec2','import-key-pair','--key-name','codyssey-b3-1','--public-key-material','fileb://'+str(key)+'.pub','--tag-specifications','ResourceType=key-pair,Tags=[{Key=Assignment,Value=B3-1}]')
save('keyPair','codyssey-b3-1')
vpc=aws('ec2','create-vpc','--cidr-block','10.31.0.0/16')['Vpc']['VpcId']; save('vpc',vpc); tag(vpc)
aws('ec2','modify-vpc-attribute','--vpc-id',vpc,'--enable-dns-hostnames','Value=true')
subnet=aws('ec2','create-subnet','--vpc-id',vpc,'--cidr-block','10.31.1.0/24')['Subnet']['SubnetId']; save('subnet',subnet); tag(subnet)
igw=aws('ec2','create-internet-gateway')['InternetGateway']['InternetGatewayId']; save('igw',igw); tag(igw)
aws('ec2','attach-internet-gateway','--vpc-id',vpc,'--internet-gateway-id',igw)
route=aws('ec2','create-route-table','--vpc-id',vpc)['RouteTable']['RouteTableId']; save('routeTable',route); tag(route)
aws('ec2','create-route','--route-table-id',route,'--destination-cidr-block','0.0.0.0/0','--gateway-id',igw)
save('routeAssociation',aws('ec2','associate-route-table','--route-table-id',route,'--subnet-id',subnet)['AssociationId'])
sg=aws('ec2','create-security-group','--vpc-id',vpc,'--group-name','codyssey-b3-1','--description','B3-1 HTTP HTTPS and source-restricted SSH')['GroupId']; save('securityGroup',sg); tag(sg)
for port, cidr in [(22,ip+'/32'),(80,'0.0.0.0/0'),(443,'0.0.0.0/0')]:
    aws('ec2','authorize-security-group-ingress','--group-id',sg,'--protocol','tcp','--port',str(port),'--cidr',cidr)
instance=aws('ec2','run-instances','--image-id','ami-083a7457bdb2d0548','--instance-type','t3.micro','--count','1','--key-name','codyssey-b3-1','--network-interfaces',json.dumps([{'DeviceIndex':0,'SubnetId':subnet,'Groups':[sg],'AssociatePublicIpAddress':True}]),'--block-device-mappings',json.dumps([{'DeviceName':'/dev/xvda','Ebs':{'VolumeSize':8,'VolumeType':'gp3','Encrypted':True,'DeleteOnTermination':True}}]),'--metadata-options','HttpTokens=required,HttpPutResponseHopLimit=1','--credit-specification','CpuCredits=standard','--user-data','file://'+str(ROOT/'infra/bootstrap.sh'),'--tag-specifications','ResourceType=instance,Tags=[{Key=Assignment,Value=B3-1},{Key=Name,Value=codyssey-b3-1}]','ResourceType=volume,Tags=[{Key=Assignment,Value=B3-1}]')['Instances'][0]['InstanceId']
save('instance',instance)
print('Provisioned. Readiness and web deployment require subsequent verification.')
