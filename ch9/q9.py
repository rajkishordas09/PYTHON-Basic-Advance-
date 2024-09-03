file1="file2.txt"
file2="copy.txt"
with open (file1) as f:
    content1=f.read()
with open (file2) as f:
    content2=f.read()

if content1==content2:
    print("files are identitical")
else :
    print("files are not identitical")        