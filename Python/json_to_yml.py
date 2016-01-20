import json 
import yaml
import sys

f = open(sys.argv[1], 'r')
jsonData = json.load(f)
f.close()

yaml.safe_dump(jsonData, file(sys.argv[2],'w'), encoding='utf-8', allow_unicode=True)
