# Usage: python boto_wipe_bucket.py my_bucket

import sys
import boto

s3_bucket = sys.argv[1]
s3 = boto.connect_s3()
bucket = s3.get_bucket(s3_bucket)
buckets_list = bucket.list()
result = bucket.delete_keys([key.name for key in buckets_list])
