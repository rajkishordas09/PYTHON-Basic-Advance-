class Employee:
    company='Microsoft'
    salary=10000
    salaryBonus=100
     
    @property   #getter method
    def totalSalary(self):
        return self.salary+self.salaryBonus

    @totalSalary.setter #also a property
    def totalSalary(self,val):
        self.salaryBonus=val-self.salary


E=Employee()        
#print(E.totalSalary())
print(E.totalSalary)#ues of property decorator
E.totalSalary=5000  #have a variabe so call 2nd method

print(E.salaryBonus)
print(Employee.salaryBonus)