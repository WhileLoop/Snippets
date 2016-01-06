# Usage: python password_verify.py password $(python password_encrypt.py password)

import sys
import hashlib
import base64

password_input = sys.argv[1]
password_encrypted = sys.argv[2]                            # Initial password is read from command line.
password_encrypted = password_encrypted[6:]                 # Strip the algorithm label.
password_encrypted = base64.b64decode(password_encrypted)   # Input is base64 decoded.
salt = password_encrypted[-8:]                              # Get the appended salt.
digest = hashlib.sha1(password_input + salt).digest()       # Hash the input password and the salt.
checkme = digest + salt;
if (checkme == password_encrypted):
  print "Match!"
else:
  print "Bad password!"
