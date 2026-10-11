from PIL import Image, ImageDraw
im=Image.new('RGB',(1400,900),'#f5f7fb');d=ImageDraw.Draw(im)
def box(rect,label,color='#dbeafe'):
 d.rounded_rectangle(rect,radius=12,fill=color,outline='#334155',width=3)
 d.text((rect[0]+20,rect[1]+18),label,fill='#101a2a',font_size=24)
d.text((45,30),'B3-1 | AWS Sydney (ap-southeast-2) | cdsy',fill='#101a2a',font_size=30)
box((300,150,1340,800),'VPC 10.31.0.0/16','#e2e8f0')
box((620,280,1270,725),'Public Subnet 10.31.1.0/24','#e0f2fe')
box((720,470,1240,650),'EC2 t3.micro / Docker Nginx + Caddy\nHTTP :80 -> Nginx | HTTPS :443 -> Caddy\nGET /health -> 200 OK\nPublic IP: 13.236.1.62','#dcfce7')
box((350,310,570,425),'Internet\nGateway')
box((620,180,1270,255),'Route Table: 0.0.0.0/0 -> IGW','#fef3c7')
box((40,320,250,430),'Internet\nBrowser / curl','#fff')
d.line((250,375,350,375),fill='#2563eb',width=7)
d.line((570,375,680,375,680,560,720,560),fill='#2563eb',width=7)
d.polygon([(720,560),(700,548),(700,572)],fill='#2563eb')
d.text((730,365),'Security Group\n80 / 443: public | 22: operator IP /32',fill='#101a2a',font_size=22)
d.text((45,825),'Seoul requirement exception: user approved Sydney. HTTPS: Caddy / Lets Encrypt.',fill='#475569',font_size=21)
from pathlib import Path
im.save(Path(__file__).resolve().parents[1]/'docs/architecture.png')
