class Employee:
    company="google"

    def __init__(n1,name,salary,subBranch):
        n1.name=name    #attributes are created which are use all methods 
        n1.salary=salary
        n1.subBranch=subBranch     
        
    def getDetails(n2):
        print(f"Employee name is : {n2.name}") 
        print(f"Employee salary is : {n2.salary}") 
        print(f"SubBranch  is : {n2.subBranch}") 



'''  def getSalary(self,name):
        print(f"{self.company} Salary is : {self.salary}\n{self.signeture} {name}")

    @staticmethod  #without argument
    def greet():
        print("Good morning Sir")'''

         
Employee1=Employee("Raj",1000000,"youTube")   #autometic called constructer
Employee1.getDetails() 

'''Employee1.salary=10000
Employee1.signeture="thanks"
Employee1.getSalary("Google")#Employee.getSalary(Employee1)
Employee1.greet()'''