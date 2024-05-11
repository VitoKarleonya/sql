import sqlite3
from two import *
 # Добавил проверки в чтобы не добавлять студентов, которые уже есть
try:
    # Подключение к базе данных
    connection = sqlite3.connect('university.db')
    cursor = connection.cursor()

    # Создание таблицы Students
    create_table_students = '''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            age INTEGER,
            city TEXT
        )
    '''
    cursor.execute(create_table_students)
    print("Таблица Students успешно создана.")

    # Добавление студентов
    students_to_add = [
        Student('Max', 'Brooks', 24, 'Spb'),
        Student('John', 'Stones', 15, 'Spb'),
        Student('Andy', 'Wings', 45, 'Manchester'),
        Student('Kate', 'Brooks', 34, 'Spb')
    ]
    for student in students_to_add:
        student.save()

    # Создание таблицы Courses
    create_table_courses = '''
        CREATE TABLE IF NOT EXISTS Course (
            id INTEGER PRIMARY KEY,
            name TEXT,
            time_start TEXT,
            time_end TEXT
        )
    '''
    cursor.execute(create_table_courses)
    print('Таблица Course успешно создана.')

    # Добавление курсов
    courses_to_add = [
        Course('Python', '13.04.2022', '15.07.2023'),
        Course('Java', '17.01.2022', '20.06.2023')
    ]
    for course in courses_to_add:
        course.save_c()

    # Создание таблицы Rel
    create_table_rel = '''
        CREATE TABLE IF NOT EXISTS Rel (
            id_course INTEGER,
            id_student INTEGER
        )
    '''
    cursor.execute(create_table_rel)
    print('Таблица Rel успешно создана.')

    # Добавление отношений
    rel_to_add = [
        Rels(1, 1),
        Rels(1, 2),
        Rels(1, 3),
        Rels(2, 4)
    ]
    for rel in rel_to_add:
        rel.save_r()


    # Получение всех студентов старше 30 лет
    query_students_over_30 = "SELECT * FROM Students WHERE age > 30"
    cursor.execute(query_students_over_30)
    results_over_30 = cursor.fetchall()
    print("Студенты старше 30 лет:")
    for row in results_over_30:
        print(row)

    # Получиение студентов, проходящих курс по Python
    query_students_python_course = """
        SELECT s.*
        FROM Students s
        JOIN Rel r ON s.id = r.id_student
        JOIN Course c ON r.id_course = c.id
        WHERE c.name = 'Python'
    """
    cursor.execute(query_students_python_course)
    results_python_course = cursor.fetchall()
    print("Студенты, проходящие курс по Python:")
    for row in results_python_course:
        print(row)

    # Получение студентов, проходящих курс по Python и из города Spb
    query_students_python_spb = """
        SELECT s.*
        FROM Students s
        JOIN Rel r ON s.id = r.id_student
        JOIN Course c ON r.id_course = c.id
        WHERE c.name = 'Python' AND s.city = 'Spb'
    """
    cursor.execute(query_students_python_spb)
    results_python_spb = cursor.fetchall()
    print("Студенты, проходящие курс по Python и из города Spb:")
    for row in results_python_spb:
        print(row)

except sqlite3.Error as e:
    print("Ошибка работы с базой данных:", e)
finally:
    if connection:
        connection.close()
