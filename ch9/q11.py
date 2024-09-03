import os

file="sample1.txt"

with open (file) as f:
    content=f.read()

with open ("sample3.txt","w") as f:
    f.write(content)

os.remove(file)    