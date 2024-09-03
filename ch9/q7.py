content=True
i=0

with open("log.txt") as f:

   while content:
    content=f.readline()#.lower()  small size
    i+=1
    if 'python' in content.lower():
      print(content)
      print(f"python is present in {i}") 
