with open ("file2.txt",'r') as f:
    content=f.read()

content=content.replace('twinkle','@@#$%$#@')
with open ("file2.txt",'w') as f:
    f.write(content)   











