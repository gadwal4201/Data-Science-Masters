import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "W7301@jqir#"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM pw2.students")
for i in mycursor.fetchall():
    print(i)
mydb.close()
print("Data retrieved successfully from pw2.students")
# This code connects to a MySQL database, retrieves data from the 'students' table in