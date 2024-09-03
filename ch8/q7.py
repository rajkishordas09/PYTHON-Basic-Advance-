
def remove (string,word):
      newstr=string.replace("raj",word)
      return newstr.strip()



this="       raj   is  a good boy         "
word="kishor"
f=remove (this,word)
print(f)
#print(f.strip())#remove only 1st space 
