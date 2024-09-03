Letter ='''Dear 
    <|NAME|>
             Your D.O.B is
                        <|DOB|>'''
a=input("Enter your name :\n")
b=input("enter your Dob :\n")
Letter=Letter.replace("<|NAME|>",a)
Letter=Letter.replace("<|DOB|>",b)
print(Letter)



