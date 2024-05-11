import sqlite3

# Подключаемся к базе данных (создаем файл базы данных, если он не существует)
conn = sqlite3.connect('university2.db')
cursor = conn.cursor()

# Создаем таблицу Students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )
''')

# Создаем таблицу Courses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY,
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
cursor.execute('''
    INSERT INTO Students (name, surname, age, city)
    VALUES ('Max', 'Brooks', 24, 'Spb')
''')

cursor.execute('''
    INSERT INTO Students (name, surname, age, city)
    VALUES ('John', 'Stones', 15, 'Spb')
''')

cursor.execute('''
    INSERT INTO Students (name, surname, age, city)
    VALUES ('Andy', 'Wings', 45, 'Manchester')
''')

cursor.execute('''
    INSERT INTO Students (name, surname, age, city)
    VALUES ('Kate', 'Brooks', 34, 'Spb')
''')

# Добавляем курсы в таблицу Courses
cursor.execute('''
    INSERT INTO Courses (name, time_start, time_end)
    VALUES ('python', '2021-07-21', '2021-08-21')
''')

cursor.execute('''
    INSERT INTO Courses (name, time_start, time_end)
    VALUES ('java', '2021-07-13', '2021-08-16')
''')

# Добавляем связи студентов с курсами в таблицу Student_courses
cursor.execute('''
    INSERT INTO Student_courses (student_id, course_id)
    VALUES (1, 1)  -- Max -> python
''')

cursor.execute('''
    INSERT INTO Student_courses (student_id, course_id)
    VALUES (2, 1)  -- John -> python
''')

cursor.execute('''
    INSERT INTO Student_courses (student_id, course_id)
    VALUES (3, 1)  -- Andy -> python
''')

cursor.execute('''
    INSERT INTO Student_courses (student_id, course_id)
    VALUES (4, 2)  -- Kate -> java
''')

# Сохраняем изменения
conn.commit()


# Выборка всех студентов
cursor.execute('SELECT * FROM Students')
students = cursor.fetchall()
print("Students:")
for student in students:
    print(student)

# Выборка всех курсов
cursor.execute('SELECT * FROM Courses')
courses = cursor.fetchall()
print("\nCourses:")
for course in courses:
    print(course)

# Выборка студентов, проходящих определенный курс
cursor.execute('''
    SELECT Students.name, Courses.name
    FROM Students
    JOIN Student_courses ON Students.id = Student_courses.student_id
    JOIN Courses ON Student_courses.course_id = Courses.id
    WHERE Courses.name = 'python'
''')
enrolled_students = cursor.fetchall()
print("\nStudents enrolled in python course:")
for student in enrolled_students:
    print(student)


