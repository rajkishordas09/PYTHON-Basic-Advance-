import json
myDict={
    "name":"rajkishor",
    "job":"student",
    22:"integer",
    "Marks":{"math":22,"english":34}
}
data=json.dumps(myDict)#convert dict. to json
print(data)
#now data is json file
data=json.dumps(myDict,indent=3,sort_keys=True)
#it error for it cannt support  int
print(data)