Story="i am Raj, My name is Rajkishor Das"
print(Story[0:5]) #Space also include

print(len(Story)) #count length


print (Story.endswith("s"))  # Return boolean 
print (Story.endswith("as"))
print (Story.endswith("Das"))
print (Story.endswith("Rajkishor Das"))

print (Story.endswith("RajkishorDas"))

print(Story.count(" "))
print(Story.count("a"))
print(Story.count("Raj"))

print(Story.capitalize())
'''Capitalize 1st letter 
         And forcefully all Letter going to be Small'''
print(Story.find("a")) #find only position of  1st a 
print(Story.find("raj"))
print(Story.find("Raj"))#find only position of  1st Raj 


print(Story.replace("Raj","W"))
#replace all Raj with W

print()




