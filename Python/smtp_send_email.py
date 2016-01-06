import smtplib

fromaddr = 'sender@mydomain.com'
toaddrs  = 'recipient@theirdomain.com'
msg = """From: sender@mydomain.com

This is the message body.
"""

smtp_server = 'email-smtp.us-east-1.amazonaws.com'
smtp_username = ''
smtp_password = ''
smtp_port = '587'

server = smtplib.SMTP(
host = smtp_server,
port = smtp_port,
local_hostname = 'mydomain.com',
timeout = 10
)
server.set_debuglevel(10)
server.starttls()
server.ehlo()
server.login(smtp_username, smtp_password)
server.sendmail(fromaddr, toaddrs, msg)
print server.quit()
