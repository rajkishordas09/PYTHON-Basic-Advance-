import json
with open ("data.json") as f:
    data=json.load(f)
print(json.dumps(data,indent=3,sort_keys=True))    
