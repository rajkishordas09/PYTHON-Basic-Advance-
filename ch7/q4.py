num=int(input("Enter the Num :"))
prime =True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
if prime :
    print(num," is a prime num")

else:
     print(num," is not a prime num")    