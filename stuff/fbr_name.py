import sqlite3


connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()


for row in rows:
	print(row)



connection.close()