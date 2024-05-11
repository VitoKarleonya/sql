import sqlite3

class DatabaseManager:
    def __init__(self, db_name='university.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print('Ошибка при выполнении запроса.', e)

    def fetch_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print('Ошибка при выполнении запроса.', e)
            return []

    def close_connection(self):
        self.connection.close()


class Student:
    db_manager = DatabaseManager()

    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city

    def student_exist(self):
        query = '''SELECT * FROM Students WHERE name = ? AND surname = ?'''
        result = self.db_manager.fetch_query(query, (self.name, self.surname))
        return len(result) > 0

    def save(self):
        if not self.student_exist():
            insert_query = '''
                INSERT INTO Students (name, surname, age, city)
                VALUES (?, ?, ?, ?)
            '''
            params = (self.name, self.surname, self.age, self.city)
            self.db_manager.execute_query(insert_query, params)
            print(f'Студент {self.name} {self.surname} успешно добавлен в базу данных.')
        else:
            print(f'Студент {self.name} {self.surname} уже существует в базе данных.')


class Course:
    db_manager = DatabaseManager()

    def __init__(self, name, time_start, time_end):
        self.name = name
        self.time_start = time_start
        self.time_end = time_end

    def courses_exist(self):
        query = '''SELECT * FROM Course WHERE name = ? AND time_start = ? AND time_end = ?'''
        result = self.db_manager.fetch_query(query, (self.name, self.time_start, self.time_end))
        return len(result) > 0

    def save_c(self):
        if not self.courses_exist():
            insert_query = '''
                INSERT INTO Course (name, time_start, time_end)
                VALUES (?, ?, ?)
            '''
            params = (self.name, self.time_start, self.time_end)
            self.db_manager.execute_query(insert_query, params)
            print(f'Курс {self.name} успешно добавлен в базу данных.')
        else:
            print(f'Курс {self.name} уже добавлен в базу данных.')


class Rels:
    db_manager = DatabaseManager()

    def __init__(self, id_course, id_student):
        self.id_course = id_course
        self.id_student = id_student

    def rel_exists(self):
        query = '''SELECT * FROM Rel WHERE id_course = ? AND id_student = ?'''
        result = self.db_manager.fetch_query(query, (self.id_course, self.id_student))
        return len(result) > 0

    def save_r(self):
        if not self.rel_exists():
            insert_query = '''
                INSERT INTO Rel (id_course, id_student)
                VALUES (?, ?)
            '''
            params = (self.id_course, self.id_student)
            self.db_manager.execute_query(insert_query, params)
            print(f'Отношение {self.id_course}, {self.id_student} успешно добавлено.')
        else:
            print(f'Отношение {self.id_course}, {self.id_student} уже существует в базе данных.')


            