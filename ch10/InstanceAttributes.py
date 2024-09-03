class Employee:
    company="google"

    def getSalary(self):
        print(f"Salary is 100k")


Emp=Employee()
Emp.getSalary()#Employee.getSalary(Emp)
print(Emp.company)
Emp.company="YouTube"
print(Emp.company)#instance variabe call 1st