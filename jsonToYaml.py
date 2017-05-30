import json, yaml
import os

json_str = { "Alphabets" : { "Capitial" : ["A", "B", "C"], "Small" : ["a", "b", "c"]}}

with open(os.getcwd() + os.path.sep + "test.yaml", "w") as f:
    yaml.dump(json_str, f, default_flow_style=False)

yaml_str = ""
with open(os.getcwd() + os.path.sep + "test.yaml", "r") as f:
    yaml_str = f.read()

print 'JSON to YAML: \n', yaml_str
print 'YAML to JSON', json.dumps(yaml.load(yaml_str), sort_keys=True, indent=2)





