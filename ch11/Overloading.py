class number:
    def __init__(self,num): 
        self.num=num
        #print("lets sum")
    def __add__(self,num1): #self=number(5), num2=number(10)
        print("Lets Add")
        return self.num+num1.num
    def __mul__(self,num2): #self=number(5), num2=number(10)
        print("Lets Multiply")
        return self.num*num2.num
    def __sub__(self,num1): #self=number(5), num2=number(10)
        print("Lets substraction")
        return self.num-num1.num
    def __truediv__(self,num1): #self=number(5), num2=number(10)
        print("Lets division")
        return self.num/num1.num

n1=number(5)        
n2=number(10)

add=n1+n2  #auto call add function becase of use '+' operator
mul=n1*n2  #auto call mul function becase of use '*' operator
sub=n1-n2  #auto call mul function becase of use '*' operator
div=n1/n2  #auto call mul function becase of use '*' operator

print(add)
print(mul)
print(sub)
print(div)