import mysql.connector
mydb=mysql.connector.connect(
 host="localhost",
 user="root",
 password="Raj@1234",
 database="PythonPrograming"
)
#print(mydb)#address

mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE PythonPrograming")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)
#mycursor.execute("CREATE TABLE Raj (name VARCHAR(300),address VARCHAR(300))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
     print(x)