def Score(n):
    return n

n=input("Enter your Num : ")
YourScore=Score(n)
  

with open('HighScore.txt') as F:
    HighScore=F.read() 

if HighScore=='':
    with open('HighScore.txt','w') as F:
        F.write(str(YourScore))

elif int(HighScore) <= int(YourScore):
      with open('HighScore.txt','w') as F:
        F.write(str(YourScore))

else:
    pass


'''def Game(n):
    return n


n=int(input("Enter the Num : "))
Score=Game(n)     
#print(type(Score))
with open('HighScore.txt') as f:
     HighScore=f.read()
if   HighScore=='':
       with open('HighScore.txt','w') as f:
              f.write(str(Score)) 
elif  int(HighScore) < Score :
        with open('HighScore.txt','w') as f:
              f.write(str(Score))        
    
else:
    pass'''