a={1,2,3,4,"raj",12.34,1,2}
a.add("kishor")
print (a)

#we cann't add list in set but add Tuple
#a.add([8,9,0]) list is unhashable

a.add((5,6,7,8))  #add tuple it is hash able

print(a)

#a.add({"raj":2}) cann't add Dictionary itis unhashable



print(len(a))
b=a.remove("raj")
print(a)

print(a.pop())#delet any element
print(a)
c=a.union({12,34})
print(c)
print(a)
