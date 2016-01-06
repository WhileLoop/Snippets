# Download a single file from S3.
# Usage: python boto_s3_download_file.py my_s3_bucket example_file.zip

import sys
from boto.s3.connection import S3Connection
from boto.s3.key import Key

s3_bucket = sys.argv[1]
filename = sys.argv[2]

conn = S3Connection()
bucket = conn.get_bucket(s3_bucket)
k = Key(bucket)
k.key = filename
k.get_contents_to_filename(filename)
