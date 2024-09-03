n=int(input("Enter the Num : "))
c=1
for i in range (1,n+1):
     c=c*i 
print(n,f" Factorial is : {c}")     


d=1
e=1

while d <=n:
     e=e*d
     d+=1     
print(n," Factorial is : ",e)
