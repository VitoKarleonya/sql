import sqlite3

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
    db_manager = DatabaseManager()

    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city

    @staticmethod
    def student_exists(name, surname):
        query = '''SELECT * FROM Students WHERE name = ? AND surname = ?'''
        result = Student.db_manager.fetch_query(query, (name, surname))
        return len(result) > 0

    def save(self):
        insert_query = '''
            INSERT INTO Students (name, surname, age, city)
            VALUES (?, ?, ?, ?)
        '''
        params = (self.name, self.surname, self.age, self.city)
        Student.db_manager.execute_query(insert_query, params)

    @staticmethod
    def add_multiple_students(students):
        students_data = [(student.name, student.surname, student.age, student.city) for student in students]
        insert_query = '''
            INSERT INTO Students (name, surname, age, city)
            VALUES (?, ?, ?, ?)
        '''
        Student.db_manager.execute_query(insert_query, students_data)

    @staticmethod
    def get_all():
        query = "SELECT * FROM Students"
        return Student.db_manager.fetch_query(query)

    @staticmethod
    def get_by_id(student_id):
        query = "SELECT * FROM Students WHERE id = ?"
        return Student.db_manager.fetch_query(query, (student_id,))
