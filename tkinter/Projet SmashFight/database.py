import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="projetLogiciel",
  password="hfX5MfGPNO6Q3mD9",
   database="SmashFight"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), score int)") 
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 
