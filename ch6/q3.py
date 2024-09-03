a=input("Enter the Text :")

if("Make a lot of Money" in a):
 spam=True
elif("Buy Now" in a):
 spam=True
elif("Subscribe now" in a):
 spam=True
elif("click it" in a):
 spam=True
else:
 spam=False

if spam:
  print("This Text is Spam") 
else:
  print("This Text is not Spam")
