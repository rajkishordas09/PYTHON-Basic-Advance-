class complex:
    def __init__(self,a,b):
        self.real=a
        self.imaginary=b

    def __add__(self,num):
        print("let's add : ")
        return f"{self.real+num.real} + {self.imaginary+num.imaginary}i"     
    
    def __str__(self):
        print("complex num is  : ")
        return f"{self.real} + {self.imaginary}i"

c1=complex(1,3)
c2=complex(4,2)
add=c1+c2 
print(add)
print(c1) # use __str__ function to print
print(c2)