import sqlite3
from sqlite3 import Error

db = ''

def create_connection(db_file):
	""" create a database connection to a SQLite database """
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
		print("Opened database successfully")
		conn.commit()
		return conn
	except Error as e:
		print(e)

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
										fname text,
										lname text,
										age integer,
										univ text,
										degree text
									); """
	
	conn = create_connection(database)
	create_table(conn,sql_student_table)
	print("Table created successfully")
	conn.commit()
	conn.close()


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

def insertStudent(database,fname1,lname1,age1,univ1,degree1):
	conn = create_connection(database)
	sql = ''' INSERT INTO student(fname,lname,age,univ,degree) VALUES(:fname,:lname,:age,:univ,:degree) '''
	cur = conn.cursor()
	cur.execute(sql,{'fname':fname1,'lname':lname1,'age':age1,'univ':univ1,'degree':degree1})
	conn.commit()
	conn.close()
	

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
    conn.commit()
    conn.close()
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
    conn.commit()
    conn.close()	
def select_student(database):
	"""
    Query student 
    :param database: database name
    :return: student
    """
	conn = create_connection(database)
	cur =  conn.cursor()
	cur.execute("SELECT * FROM student")
	student = cur.fetchone()
	conn.commit()
	return student

