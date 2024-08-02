import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="siddharth",
  password="@sidhu2003"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE std_database")