#DRY princeple
class Employee:
    company='Google'

    def showDetails(self):
        print("this is an Employee")    

class Programmer(Employee):
    language='Python'

    def getLanguage(self):
        print(f"The language is : {self.language}")

    def showDetails(self):
        print("this is an Programmer") 


E=Employee()
P=Programmer()

P.getLanguage()
P.showDetails()

print(P.company)
print(P.language)