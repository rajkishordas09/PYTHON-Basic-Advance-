def sumNum(n):
    if n==1:
        return 1
    if n==0:
        return 0    
    return n+sumNum(n-1)

n=int(input("Enter num : "))
sums=sumNum(n)
print(sums)

a="abcd"
for i in a:
    print(i.upper())