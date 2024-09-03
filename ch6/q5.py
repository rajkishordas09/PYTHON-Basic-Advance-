marks=int(input("enter your Marks \n"))

if marks>=90:
    grade="O"
elif marks>=80:
    grade="A"
elif marks>=70:
    grade="B"
elif marks>=50:
    grade="C"
elif marks>=33:
    grade= "D"    
else :
   grade="F"

print("Your Grade is :" + grade)    
