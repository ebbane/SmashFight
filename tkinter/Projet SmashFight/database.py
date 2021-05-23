import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error



def disp():
    try:
        mySQLconnection = mysql.connector.connect(
                                host="localhost",
                                user="projetLogiciel",
                                password="hfX5MfGPNO6Q3mD9",
                                database="SmashFight"
        )

        sql_select_Query = "SELECT * FROM users ORDER BY score DESC"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        print("Total number of rows in student is - ", cursor.rowcount)
        print ("Printing each row's column values i.e.  student record")

        for row in records:
            print(row[0],"\t",row[1],"\t""\n")

        cursor.close()
    
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")

def insert(name,score):
    global x
    try:
       connection = mysql.connector.connect(
                                host="localhost",
                                user="projetLogiciel",
                                password="hfX5MfGPNO6Q3mD9",
                                database="SmashFight"
        )

    
       sql_insert_query = ("INSERT INTO users(name, score) VALUES (%s,%s)", (name, score))

       cursor = connection.cursor()
       result  = cursor.execute(*sql_insert_query)
       connection.commit()
       print ("Succes")

    except mysql.connector.Error as error :
        connection.rollback() #rollback if any exception occured
        print("Failed inserting record into users table {}".format(error))

    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def update(name,score):
    try:
       connection = mysql.connector.connect(
                                host="localhost",
                                user="projetLogiciel",
                                password="hfX5MfGPNO6Q3mD9",
                                database="SmashFight"
        )

       cursor = connection.cursor()

       #Update single record now
       sql_update_query = "Update users set score = '' where name = '' "
       cursor.execute(sql_update_query)
       connection.commit()
       print ("Record Updated successfully ")

       

    except mysql.connector.Error as error :
        print("Failed to update record to database: {}".format(error))
        connection.rollback()

    finally:
        #closing database connection.
        if(connection.is_connected()):
            connection.close()
            print("connection is closed")