import json

handle = open("/tmp/jsonFile")

records = [ json.loads(lines) for lines in handle]

print (json.dumps(records, indent=6, sort_keys=True))
