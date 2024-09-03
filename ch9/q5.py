words=['apple','grapes','banana']

with open ("file3.txt",'r') as f:
    content=f.read()
for word in words:
    content=content.replace(word,"@#$%@#$%")
    with open ("file3.txt",'w') as f:
         f.write(content)