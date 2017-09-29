import sqlite3
from sqlite3 import Error

db = ''

def create_connection(db_file):
	""" create a database connection to a SQLite database """
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
		print("Opened database successfully")
		db = db_file
		return conn	
	except Error as e:
		print(e)
	return None

def create_table(conn, create_table_sql):
	""" create a table from the create_table_sql statement
	:param conn: Connection object
	:param create_table_sql: a CREATE TABLE statement
	:return:
	"""
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def create_student_table(database):
	sql_student_table = """ CREATE TABLE IF NOT EXISTS student (
										id integer PRIMARY KEY,
										fname text NOT NULL,
										lname text NOT NULL,
										age integer,
										univ text NOT NULL,
										degree text NOT NULL
									); """
	
	conn = create_connection(database)
	create_table(conn,sql_student_table)
	print("Table created successfully")


def insert(conn,student):
	"""
	Create a new student into the students table
	:param conn:
	:param student:
	:return: student id
	"""
	sql = ''' INSERT INTO student (fname,lname,age,univ,degree) VALUES(?,?,?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, student)
	return cur.lastrowid

def insertStudent(database,fname,lname,age,univ,degree):
	conn = create_connection(database)
	try:
		student = (fname,lname,age,univ,degree)
		id = insert(conn,student)
		print("Insering Done ! id = "+id)
	except Error as e:
		print(e)

def delete_all(database):
    """
    Delete all rows in the tasks table
    :param database: the SQLite database name
    :return:
    """
    conn = create_connection(database)
    sql = 'DELETE FROM student'
    cur = conn.cursor()
    cur.execute(sql)

def update_task(conn, student):
    """
    update fname, lname,age,univ, and degree of a student
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' UPDATE student
              SET fname = ? ,
                  lname = ? ,
                  age = ? ,
                  univ = ? ,
                  degree = ?,
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, student)