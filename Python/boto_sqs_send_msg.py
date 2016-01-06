import boto
from boto.sqs.message import RawMessage

sqs_queue_name = ''
message_body = ''

sqs = boto.connect_sqs()
q = sqs.get_queue(message_body)
m = RawMessage()
m.set_body(message_body)
q.write(m)
