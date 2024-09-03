def f1(n):
    return lambda a,b:a*b
def f2(n):
    return lambda a,b,c:a*b*c+n


x1=f1(5)
print(x1(4,5))
x2=f2(4)
print(x2(4,5,6))