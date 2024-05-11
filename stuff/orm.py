import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
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

class Model:
    db_manager = DatabaseManager('database.db')

class Student(Model):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        query = "INSERT INTO students (name, age) VALUES (?, ?)"
        self.db_manager.execute_query(query, (self.name, self.age))

    @classmethod
    def find_by_name(cls, name):
        query = "SELECT * FROM students WHERE name = ?"
        result = cls.db_manager.fetch_query(query, (name,))
        if result:
            return cls(*result[0])
        return None

# Использование ORM
# Создание таблицы students
Model.db_manager.execute_query('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Создание и сохранение студента
student1 = Student('John', 20)
student1.save()

# Поиск студента по имени
found_student = Student.find_by_name('John')
if found_student:
    print(f"Found student: {found_student.name}, {found_student.age}")
else:
    print("Student not found")
