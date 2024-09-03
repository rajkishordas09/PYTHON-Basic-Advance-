def maximum(n1,n2,n3):
    if n1<n2:
        if n2<n3:
            return n3
        else:
            return n2    
    else:
        if n1<n3:
            return n3
        else :
            return n1    


n1=int(input("Enter num1 : "))
n2=int(input("Enter num2 : "))
n3=int(input("Enter num3 : "))
Maxi=maximum(n1,n2,n3)           
print(f"Largest Num is : {Maxi}")
#print ("Largest num is : "+str(Maxi))

