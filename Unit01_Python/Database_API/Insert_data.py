import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "W7301@jqir#"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS pw2.students(Name VARCHAR(50), Age INT, Grade VARCHAR(10))")
mycursor.execute("INSERT INTO pw2.students (Name, Age, Grade) VALUES (%s, %s, %s)", ("John Doe", 20, "A"))
mydb.commit()
mydb.close()
print("Data inserted successfully into pw2.students")
# This code connects to a MySQL database, creates a table if it doesn't exist, and