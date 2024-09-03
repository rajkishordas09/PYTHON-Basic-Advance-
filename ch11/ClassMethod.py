#For change class attributes.......
class Employee :
    company='Microsoft'
    salary=1000000
    location='Bangaluru'
     
    # def changeSalary(self,sal):
    #    self.salary=sal
    #    self.__class__.salary=sal

    @classmethod
    def changeSalary(self,sal):
          self.salary=sal

E=Employee()        
E.changeSalary(10000)
print(E.salary)
print(Employee.salary)