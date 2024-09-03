#--->Rock paper Scissors <---
import random

def GameWin(Comp,You):
    if Comp == You:
          return None
    elif Comp == 'R':
        if  You == 'P':
            return True 
        else:
            return False         
    elif Comp == 'P':
        if  You == 'S':
            return True
        else:
            return False          
    elif Comp == 'S':
        if  You == 'R':
            return True 
        else:
            return False         


A="---> Rock(R) Paper(P) Scissors(S) <--- "
You=input("Enter your Turn : ")
 
RandNo=random.randint(1,3) 
if RandNo==1:
    Comp='R' 
elif RandNo==2:
    Comp='P' 
else :
    Comp='S' 

print(A)    
print(f"Computer Turn : {Comp}")
print(f"Your Turn : {You}")

Win=GameWin(Comp,You)

if Win == None:
    print("Game is Tie")
elif Win:
    print("You Win ")    
else :
    print("You Lose")    



