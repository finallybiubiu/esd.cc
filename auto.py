import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "esdcc.settings")
django.setup()
import json
from main.models import Segmentfault as S
from main.models import Segmentfault_Blog as SB

data = []
with open('/var/www/esd.cc/segmentfault.json') as f:
 for i in f:
  data.append(json.loads(i)['result'])

for i in data:
 S.objects.create(
title=i['title'],
qid=i['url'][-16:],
author=i['author'],
mark=i['mark'],
view=i['view'],
follow=i['follow'],
)


data=[]
with open('/var/www/esd.cc/segmentfault_blog.json') as f:
 for i in f:
  data.append(json.loads(i)['result'])

for i in data:
 SB.objects.create(
title=i['title'],
bid=i['url'][-16:],
author=i['author'],
mark=i['mark'],
name=i['url'].replace('http://segmentfault.com/blog/','')[:-17],
view=i['view'],
recommend=i['recommend'],
)


