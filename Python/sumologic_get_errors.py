# Use the Sumologic API to query for errors and print a html report.

import requests
import json
import time
import sys
from datetime import date
from datetime import timedelta

session = requests.Session()
session.auth = ('', '')
session.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}


yesterdays_date = str(date.today() - timedelta(days=1))

query_string = sys.argv[1]
time_from = yesterdays_date + 'T00:00:00'
time_to = yesterdays_date + 'T23:59:59'
timezone = 'EST'

payload = json.dumps({'query': query_string, 'from': time_from, 'to': time_to, 'timeZone': timezone})
print payload

response = session.post('https://api.sumologic.com/api/v1/search/jobs', data=payload)
print response.text

job_id = response.json()['id']

print job_id
job_status = ''
while(job_status != 'DONE GATHERING RESULTS'):
    time.sleep(15)
    resp = session.get("https://api.sumologic.com/api/v1/search/jobs/" + job_id)
    job_status = resp.json()['state']
    message_count = resp.json()['messageCount']
    records_count = resp.json()['recordCount']
    print message_count

print job_status
print records_count

offset = 0
limit = records_count

messages = session.get("https://api.sumologic.com/api/v1/search/jobs/" + job_id + '/records', params={'offset': offset, 'limit': limit})
messages_json = json.loads(messages.text)

actual_messages =  messages_json['records']

actual_messages.sort(key=lambda e: int(e['map']['_count']), reverse=True)

f = open('error_summary.html','w')
f.write('<style>tr:nth-child(even){background:#CCC}td{padding:10px}div{padding:10px}</style>')
f.write('<div>' + query_string + ' ' + time_from + ' -  ' + time_to + ' ' + timezone + '</div>')
f.write('<table><thead><th>Count</th><th>Signature</th></thead><tbody>')

for m in actual_messages:
    signature =  m['map']['_signature']
    signature = signature.replace('$DATE', '')
    f.write('<tr>')
    f.write('<td>' + m['map']['_count'] + '</td>')
    sig = '<td>' + signature + '</td>'
    f.write(sig.encode('utf8'))
    f.write('</tr>')
f.write('</tbody></table>')

g = open('error_count.txt', 'w')
g.write(str(message_count))
