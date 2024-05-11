

import sqlite3
PRAGMA table_info(Students);

# Создаем подключение к базе данных
connection = sqlite3.connect('university.db')
cursor = connection.cursor()

# SQL-запрос для создания таблицы Students
create_table_query = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        age INTEGER,
        city TEXT
    )
'''

# Выполняем запрос
cursor.execute(create_table_query)

# Сохраняем изменения
connection.commit()

# Закрываем соединение
connection.close()
