Sub1=int(input("Enter 1st Sub Mark :"))
Sub2=int(input("Enter 2st Sub Mark :"))
Sub3=int(input("Enter 3st Sub Mark :"))
Sub4=int(input("Enter 4st Sub Mark :"))

if Sub1<30 or Sub2<30 or Sub3<30 or Sub4<30:
    print("You are Fail due to less than of Passing Marks")
elif (Sub1+Sub2+Sub3+Sub4)/4<40:
    print("You are Fail due to less than 40'%' of Total Marks")    
else:
    print("Congratulations You are Passed")    