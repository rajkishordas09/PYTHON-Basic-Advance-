with open ('file.txt','r') as f:
    content=f.read()

with open('copy.txt','w') as f:
     f.write(content)
