import sqlite3

# Установка соединения с базой данных
conn = sqlite3.connect('example.db')

# Создание объекта курсора
cursor = conn.cursor()

# Исполнение запроса SQL с помощью курсора
cursor.execute('SELECT * FROM Students')

# Получение результатов запроса
rows = cursor.fetchall()

# Вывод результатов
for row in rows:
    print(row)

# Закрытие соединения с базой данных
conn.close()
