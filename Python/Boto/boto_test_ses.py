import boto.ses

conn = boto.ses.connect_to_region('us-east-1')

conn.send_email(
  'sender@mydomain.com',
  'Subject',
  'Body',
  ['recipient@theirdomain.com'])
