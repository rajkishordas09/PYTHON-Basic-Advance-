class Number:
    def __init__(self,num): 
        self.num=num

    def __str__(self):
        return f"Number is {self.num}"

    def __len__(self):
        return 89    


n=Number(8)
print(n)        
print(len(n))
print(type(len(n)))