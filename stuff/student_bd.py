import sqlite3
from personal__orm import *

# Инициализация менеджера базы данных
db_manager = DatabaseManager()


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


# Пример использования ORM для работы с данными
try:
    # Создание и сохранение студентов
    students = [
        ('Max', 'Brooks', 24, 'Spb'),
        ('John', 'Stones', 15, 'Spb'),
        ('Andy', 'Wings', 45, 'Manchester'),
        ('Kate', 'Brooks', 34, 'Spb')
    ]

    student_exists(students)
    add_student(students)


    # Получение всех студентов из базы данных
    all_students = Student.get_all()
    print("All Students:")
    for student in all_students:
        print(f"ID: {student.id}, Name: {student.name}, Surname: {student.surname}, Age: {student.age}, City: {student.city}")

        # # Создание и сохранение курсов
        # courses_data = [
        #     ('python', '2021-07-21', '2021-08-21'),
        #     ('java', '2021-07-13', '2021-08-16')
        # ]

        # for course_info in courses_data:
        #     course = Course(*course_info)
        #     course.save()

        # # Создание и сохранение связей студентов с курсами
        # student_course_data = [
        #     (1, 1),  # Max -> python
        #     (2, 1),  # John -> python
        #     (3, 1),  # Andy -> python
        #     (4, 2)   # Kate -> java
        # ]

        # for student_course_info in student_course_data:
        #     student_id, course_id = student_course_info
        #     existing_relationship = StudentCourse.get_by_student_id_course_id(student_id, course_id)
        #     if not existing_relationship:
        #         student_course = StudentCourse(student_id, course_id)
        #         student_course.save()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Закрытие соединения с базой данных
    db_manager.close_connection()
