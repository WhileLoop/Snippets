import json
import yaml
import sys

f = open(sys.argv[1], 'r')
yaml_data = yaml.load(f)
f.close()

output_file = open(sys.argv[2], "w")
json_data = json.dumps(yaml_data, indent=4)
output_file.write(json_data)
output_file.close()
