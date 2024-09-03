def fun(variable): 
  letters = ['a', 'e', 'i', 'o', 'u']
  if (variable in letters): 
    return True 
  else: 
    return False 
# return only True values 

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun, sequence) 
print('The filtered letters are:') 
# print(list(filtered))
for s in filtered:
   print(s)

# def odd(x):
#    for a in range(2,x):
#         if (x%a!=0):
#           return True
#         else:
#           return False
          

# f=filter(odd,range(21))#call function and iterator
# print(list(f))#it print only true value