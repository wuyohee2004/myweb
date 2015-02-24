import db_connector
import json
from django.utils import simplejson
b=db_connector.OpsLogTemp.objects.filter(track_mark=18).values('ip','event_log')
print type(b)
#print simplejson.dumps(b)
data_dic = {}
for i in b:
	print i['ip']
	#for line in  str(i['event_log']).split('\\n'):
	#	rint line
	data_dic[i['ip']] = str(i['event_log']).split('\\n')

print json.dumps(data_dic)
