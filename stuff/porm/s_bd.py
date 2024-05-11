

from two import *

# Создаем подключение к базе данных
connection = sqlite3.connect('university.db')
cursor = connection.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        age INTEGER,
        city TEXT
    )
'''

try:
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица Students успешно создана или уже существует.")
except Exception as e:
    print("Ошибка при создании таблицы Students:", e)
finally:
    connection.close()

# Список студентов для добавления
students_to_add = [
    Student('Max', 'Brooks', 24, 'Spb'),
    Student('John', 'Stones', 15, 'Spb'),
    Student('Andy', 'Wings', 45, 'Manchester'),
    Student('Kate', 'Brooks', 34, 'Spb')
]

# Добавляем студентов в базу данных
for student in students_to_add:
    student.save()

# Получаем всех студентов из базы данных и выводим их информацию
connection = sqlite3.connect('university.db')
cursor = connection.cursor()

all_students = cursor.execute("SELECT * FROM Students").fetchall()
print("All Students:")
for student in all_students:
    print(f"ID: {student[0]}, Name: {student[1]}, Surname: {student[2]}, Age: {student[3]}, City: {student[4]}")

connection.close()


