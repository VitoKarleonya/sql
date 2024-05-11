import sqlite3

class DatabaseManager:
	def __init__(self,db_name='university.db'):
		self.db_name = db_name
		self.connection = sqlite3.connect(self.db_name)
		self.cursor = self.connection.cursor()

	def execute_query(self,query,params=None):
		try:
			if params:
				self.cursor.execute(query,params)
			else:
				self.cursor.execute(query)
			self.connection.commit()
		except Exception as e:
			print('Ошибка при выполнении запроса.', e)

	def fetch_query(self,query,params=None):
		try:
			if params:
				self.cursor.execute(query,params)
			else:
				self.cursor.execute(query)
			return self.cursor.fetchall()
		except Exception as e:
			print('Ошибка при выполнении запроса.', e)
			return []

	def close_connection(self):
		self.connection.close()


class Student:
	db_manager =DatabaseManager()

	def __init__(self,name,surname,age,city):
		self.name = name
		self.surname = surname
		self.age = age
		self.city = city

	def student_exist(self):
		query = ''' SELECT * FROM Students WHERE name = ? AND surname = ?'''
		result = self.db_manager.fetch_query(query,(self.name,self.surname))
		return len(result) > 0


	def save(self):
		if not self.student_exists():
			insert_query = '''
				INSERT INTO Students (name,surname,age,city)
				VALUES (?,?,?,?)
			'''
			params = (self.name,self.surname,self.age,self.city)
			self.db_manager.execute_query(insert_query,params)
			print(f'Студент{self.name}{self.surname} успешно добавлен в базу данных.')
		else:
			print(f'Студент{self.name}{self.surname} уже стуществует в базе данных.')
			