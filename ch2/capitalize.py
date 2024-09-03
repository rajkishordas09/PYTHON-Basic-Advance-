names = input("Enter a list of names separated by spaces: ").split()
#delet .split()#--->capitalize all word
capitalized_names = [name.capitalize() for name in names]
print("Capitalized names:")
for name in capitalized_names:
    print(name,end=" ")
print("\n",type(capitalized_names))
#if print in list
#print(capitalized_names)