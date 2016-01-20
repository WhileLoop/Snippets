# Usage: python boto_s3_presigned_url.py my_bucket my_file.zip

import sys
from boto.s3.connection import S3Connection

s3_bucket = sys.argv[1]
s3_filename = sys.argv[2]

connection = S3Connection()
print connection.generate_url(960, 'GET', bucket=s3_bucket, key=s3_filename)
