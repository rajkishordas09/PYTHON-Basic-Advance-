class C2dVec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):#return string
         return f"vector is: {self.icap}i + {self.jcap}j"
      
class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return f"vector is: {self.icap}i + {self.jcap}j + {self.kcap}k"     


V1=C2dVec(1,2)   
V2=C3dVec(3,4,5)   
print(V1)
print(V2)