import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", passwd="Ashu2124#", database="schooldb")

my_cursor = my_db.cursor()

# mycursor.execute("show databases")
my_cursor.execute("select * from employee")

# result = my_cursor.fetchall()
result = my_cursor.fetchone()

for i in result:
    print(i)


