myDict={
    "Fast":"quick",
    "First":"top",
    "Trust":"belive",
    22:"raj",
    "Marks":[1,2,3,4,5,6,7],
    "No":(1,2,3,4,4),
    "Dict2":{"Love":"Trust"}
}
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(list(myDict.keys()))

print(type(myDict.keys()))

#UpdateDictionary with adding

updateDict={
    
    "Raj":"Kishor",#new add
     "Fast":"ready"#updated old value
   
}
myDict.update(updateDict)
print(myDict)

#print(myDict["Love"])#error
print(myDict["Dict2"]["Love"])
print(myDict.get("raj"))
#print(myDict["raj"]) #through error 