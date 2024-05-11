import sqlite3

# Подключаемся к базе данных (создаем файл базы данных, если он не существует)
conn = sqlite3.connect('university22.db')
cursor = conn.cursor()

# Создаем таблицу Students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )
''')

# Создаем таблицу Courses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time_start TEXT,
        time_end TEXT
    )
''')

# Создаем таблицу Student_courses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student_courses (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students(id),
        FOREIGN KEY (course_id) REFERENCES Courses(id),
        PRIMARY KEY (student_id, course_id)
    )
''')

# Сохраняем изменения
conn.commit()

# Добавляем данные в таблицу Students
students_data = [
    ('Max', 'Brooks', 24, 'Spb'),
    ('John', 'Stones', 15, 'Spb'),
    ('Andy', 'Wings', 45, 'Manchester'),
    ('Kate', 'Brooks', 34, 'Spb')
]

for student in students_data:
    cursor.execute('''
        INSERT INTO Students (name, surname, age, city)
        VALUES (?, ?, ?, ?)
    ''', student)

# Добавляем данные в таблицу Courses
courses_data = [
    ('python', '2021-07-21', '2021-08-21'),
    ('java', '2021-07-13', '2021-08-16')
]

for course in courses_data:
    cursor.execute('''
        INSERT INTO Courses (name, time_start, time_end)
        VALUES (?, ?, ?)
    ''', course)

# Добавляем связи студентов с курсами в таблицу Student_courses
student_course_data = [
    (1, 1),  # Max -> python
    (2, 1),  # John -> python
    (3, 1),  # Andy -> python
    (4, 2)   # Kate -> java
]

for sc in student_course_data:
    cursor.execute('''
        INSERT INTO Student_courses (student_id, course_id)
        VALUES (?, ?)
    ''', sc)

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()
