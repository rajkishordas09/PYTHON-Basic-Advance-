'''n=int(input("Enter the Num : "))
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
'''
def recursive_factorial(n):
      if n==1 or n==0:
           return 1
      return n*recursive_factorial(n-1)

n=int(input("Enter num : "))
f=recursive_factorial(n)
print(f"Factorial is : {f}")