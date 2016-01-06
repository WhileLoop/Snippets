# Generate a salted, SHA1 encrypted password in base64.

import os
import sys
import hashlib
import base64

password = sys.argv[1]								              # Initial password is read from command line.
salt = os.urandom(8)                                # Generate random 8 byte salt string.
digest = hashlib.sha1(password + salt).digest()     # Append the salt to the password, then SHA1 hash.
digest_salt = digest + salt							            # Append the salt to the digest. This is so the salt can be seen during verification.
encoded = base64.b64encode(digest_salt)             # Base64 encode for compact database storage.
print '{SSHA}' + encoded								            # Append digest type to output string so verification knows which alogrithm to use.
