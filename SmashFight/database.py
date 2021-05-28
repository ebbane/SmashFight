import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="projetLogiciel",
  password="hfX5MfGPNO6Q3mD9"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE SmashFight")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x) 


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="projetLogiciel",
#   password="hfX5MfGPNO6Q3mD9"
# )

# cursor = mydb.cursor()
# cursor.execute("CREATE TABLE users (name VARCHAR(255), score INT))")
