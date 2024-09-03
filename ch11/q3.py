class Employee:
       salary=10000
       increment=2.5

       @property
       def salaryAfterIncrement(self):
           return self.salary*self.increment
       
       @salaryAfterIncrement.setter
       def salaryAfterIncrement(self,sai):
           self.increment=sai/self.salary


E=Employee()    
print(E.salaryAfterIncrement)
E.salaryAfterIncrement=30000
print(E.increment)