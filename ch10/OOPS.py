#DRY=don't repeat yourself
'''a=12
b=34
print(f"Sum of a and b: {a+b}")'''

class Sum:
    def NumSum(num):
        return num.a+num.b

add=Sum()        
add.a=12
add.b=34
A=add.NumSum()
print(f'sum is : {A}')