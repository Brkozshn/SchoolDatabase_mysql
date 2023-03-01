import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",  #192.23.45.56 gibi bir tane firmadan almak gerek
    user="root",
    password="Burak3461*",
    database="node_app"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255) )")  #tablo oluşturma

#mycursor.execute("SHOW DATABASES")
mycursor.execute("CREATE DATABASE mydatabase") #databasae oluşturma

#for x in mycursor:

