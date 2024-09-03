class Employee:
    company="google"

    def getSalary(self,name):
        print(f"{self.company} Salary is : {self.salary}\n{self.signeture} {name}")

    @staticmethod  #without argument
    def greet():
        print("Good morning Sir")

    
         
Employee1=Employee()
Employee1.salary=10000
Employee1.signeture="thanks"
Employee1.getSalary("Google")#Employee.getSalary(Employee1)
Employee1.greet()