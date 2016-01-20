# Prints a list of all access keys with the associated user.

import boto
from boto.iam.connection import IAMConnection

cfn = IAMConnection()
data = cfn.get_all_users()
for user in data.list_users_result.users:
  for ak in cfn.get_all_access_keys(user.user_name).list_access_keys_result.access_key_metadata:
    print user.user_name + ': ' + ak.access_key_id
