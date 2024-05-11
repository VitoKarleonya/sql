import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

createTable = '''CREATE TABLE Users(firstName varchar(32),lastName varchar(32), age int)'''
cursor.execute('''DROP TABLE IF EXISTS Users''')
cursor.execute(createTable)


newUsers = [
('Max', 'Adams', 16),
('John', 'Smith', 23),
('Adam', 'Brooks', 48),]

cursor.executemany("Insert into Users values (?,?,?);", newUsers)

connection.commit()
connection.close()
