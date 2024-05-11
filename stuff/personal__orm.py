class DatabaseManager:
    def __init__(self, db_name='university.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()


    def fetch_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()



class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city


    def student_exists(name, surname):
    query = "SELECT * FROM Students WHERE name = ? AND surname = ?"
    result = db_manager.fetch_query(query, (name, surname))
    return len(result) > 0



    def save(self):
        # Создаем подключение к базе данных
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        # SQL-запрос для добавления студента
        insert_query = '''
            INSERT INTO Students (name, surname, age, city)
            VALUES (?, ?, ?, ?)
        '''

        # Выполняем запрос с данными текущего студента
        cursor.execute(insert_query, (self.name, self.surname, self.age, self.city))

        # Сохраняем изменения
        conn.commit()

        # Закрываем соединение
        conn.close()



    @staticmethod
    def add_multiple_students(students):
        # Создаем подключение к базе данных
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        # Список данных для всех студентов
        students_data = [(student.name, student.surname, student.age, student.city) for student in students]

        # SQL-запрос для добавления студентов
        insert_query = '''
            INSERT INTO Students (name, surname, age, city)
            VALUES (?, ?, ?, ?)
        '''

        # Выполняем массовое добавление студентов
        cursor.executemany(insert_query, students_data)

        # Сохраняем изменения
        conn.commit()

        # Закрываем соединение
        conn.close()
    


    @staticmethod
    def get_all():
        query = "SELECT * FROM Students"
        return db_manager.fetch_query(query)

    @staticmethod
    def get_by_id(student_id):
        query = "SELECT * FROM Students WHERE id = ?"
        return db_manager.fetch_query(query, (student_id,))




    def update(self):
        query = "UPDATE Students SET name=?, surname=?, age=?, city=? WHERE id=?"
        db_manager.execute_query(query, (self.name, self.surname, self.age, self.city, self.id))

    def delete(self):
        query = "DELETE FROM Students WHERE id=?"
        db_manager.execute_query(query, (self.id,))




class Course:
    def __init__(self, name, time_start, time_end):
        self.name = name
        self.time_start = time_start
        self.time_end = time_end

    def save(self):
        query = "INSERT INTO Courses (name, time_start, time_end) VALUES (?, ?, ?)"
        db_manager.execute_query(query, (self.name, self.time_start, self.time_end))

    def course_exists(course_name):
    query = "SELECT * FROM Courses WHERE name = ?"
    result = db_manager.fetch_query(query, (course_name,))
    return len(result) > 0

    def add_course(courses):
        if not Course.course_exists(name,time_start,time_end):
            new_course = Course(name,time_start,time_end)
            new_course.save()
            print(f"Курс {name} успешно добавлен в базу данных.")
        else:
            print(f"Курс {name} уже существует в базе данных. Дублирование данных.")







    @staticmethod
    def get_all():
        query = "SELECT * FROM Courses"
        return db_manager.fetch_query(query)

    @staticmethod
    def get_by_id(course_id):
        query = "SELECT * FROM Courses WHERE id = ?"
        return db_manager.fetch_query(query, (course_id,))




    def update(self):
        query = "UPDATE Courses SET name=?, time_start=?, time_end=? WHERE id=?"
        db_manager.execute_query(query, (self.name, self.time_start, self.time_end, self.id))

    def delete(self):
        query = "DELETE FROM Courses WHERE id=?"
        db_manager.execute_query(query, (self.id,))





class StudentCourse:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    def save(self):
        query = "INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)"

        # Проверяем, что такая комбинация (student_id, course_id) не существует
        check_query = "SELECT * FROM Student_courses WHERE student_id = ? AND course_id = ?"
        existing_record = db_manager.fetch_query(check_query, (self.student_id, self.course_id))

        if not existing_record:
            db_manager.execute_query(query, (self.student_id, self.course_id))
        else:
            print(f"Student with ID {self.student_id} is already enrolled in Course with ID {self.course_id}")

    def student_course_relation_exists(student_id, course_id):
    query = "SELECT * FROM Student_courses WHERE student_id = ? AND course_id = ?"
    result = db_manager.fetch_query(query, (student_id, course_id))
    return len(result) > 0

    def student_course_add(student_id,course_id):
        if not student_course_relation_exists(student_id,course_id):
            new_rel = StudentCourse(student_id,course_id)
            new_rel.save()
            print("Связи добавлены.")
        else:
            print("Связи уже существуют. Дублирование данных.")







    # Остальные методы класса StudentCourse оставляются без изменений
    @staticmethod
    def get_all():
        query = "SELECT * FROM Student_courses"
        return db_manager.fetch_query(query)

    @staticmethod
    def get_by_student_id(student_id):
        query = "SELECT * FROM Student_courses WHERE student_id = ?"
        return db_manager.fetch_query(query, (student_id,))

    @staticmethod
    def get_by_course_id(course_id):
        query = "SELECT * FROM Student_courses WHERE course_id = ?"
        return db_manager.fetch_query(query, (course_id,))





    def delete(self):
        query = "DELETE FROM Student_courses WHERE student_id=? AND course_id=?"
        db_manager.execute_query(query, (self.student_id, self.course_id))




db_manager = DatabaseManager()
