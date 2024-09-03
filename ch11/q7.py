class vector:
    def __init__(self,vec):
         self.vec=vec
    

    def __add__(self,vec1):
        vec2=[]
        for i in range(len(self.vec)):
            vec2.append(f"{self.vec[i]+vec1.vec[i]}") #append use for list
        return vector(vec2)#it use str to print

    def __mul__(self,vec1):
        sum=0
        for i in range(len(self.vec)):
            sum+=self.vec[i]*vec1.vec[i]
        return sum

    def __str__(self):
        str=''    
        c=0
        for i in self.vec:
            str+=f" {i}a{c} +"
            c+=1
        return str[:-1]
    
    def __len__(self):
        return len(self.vec)

v1=vector([1,2,3])       
v2=vector([4,5,6,5])
'''v=v1+v2
print(f"sum of the vector is : {v}") 
v3=v1*v2
print(f"dot product is : {v3}")'''
print(len(v1))
print(len(v2))