class person:
    country='India'
    bonus =2345
    def __init__(self):
        print(f"My country is {self.country}")
    def takeBreath(self):
        print("I am breathing..")

    def getSalary(self):
        print(f"salary is ")    

class Employee(person):
    company='Google'
    bonus =234
    def getSalary(self):
        super().__init__()
       # super().takeBreath()
        print(f"salary is {self.salary}")

    def getBonus(self):
       print(f"my Bonus is {self.bonus} and salary is {self.salary} ")    

    def takeBreath(self):
        print("I am also breathing..")

class Programmer(Employee):
    language='Python'        
    salary=10000
    bonus =23456
    
    def getSalary(self):
        #super().__init__()
        super().getSalary()
        print("no salary")
    def takeBreath(self):
       print("Programmer  also breathing..")

P=Programmer()   
#P.takeBreath() 
#E=Employee()
P.getSalary()
#P.getBonus()