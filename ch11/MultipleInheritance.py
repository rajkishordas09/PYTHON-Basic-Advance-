# 2 or more parents but single child
class Employee:
    company='Google'

    def __init__(self,name,id):
        self.id=id
        self.name=name
    def showDetails(self):
        print(f"this is an Employee\nhis company is : {self.company}\nMy name is {self.name} and Id : {self.id}")  


class Freelancer:
    company='Fiverr'
    language='Python'
    def showDetails(self,id):
        print(f"this is an Employee\nhis company is : {self.company} and Id : {id}")  
    
    def getLanguage(self):
        print(f"The language is : {self.language}")

class Programmer(Employee,Freelancer):  #here Employee class is priority than class Freelancer
   

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def showDetails(A):
      print(f"this is an Programmer.\nhis name is {A.name} and salary is : {A.salary}") 
        
    

P=Programmer('RAJ',1000000)
P.showDetails()
P.getLanguage()
print(P.company) #Employee is more priority because write 1st
print('---->--------------->----------->----')
F=Freelancer()
F.showDetails(2141004150)
print('---->--------------->----------->----')
E=Employee('KISHOR',2141004150)
E.showDetails()