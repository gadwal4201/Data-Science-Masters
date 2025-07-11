import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "W7301@jqir#"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS pw2")
mydb.close()
print("Database created successfully")