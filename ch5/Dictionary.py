myDict={
    "Fast":"quick",
    "First":"top",
    "Trust":"belive",
    22:"raj",
    "Marks":[1,2,3,4,5,6,7],
    "No":(1,2,3,4,4),
    "Dict2":{"Love":"Trust",}
}
print(myDict[22])
print(myDict['''Fast'''])
print(myDict['First'])
print(myDict["Marks"])
print(myDict["No"])
print(myDict["Dict2"])
print(myDict["Dict2"]["Love"])

#Dictionary is Muteable
myDict["Love"]={"Trust":"Belives"}
print(myDict["Love"])
print(myDict["Trust"])