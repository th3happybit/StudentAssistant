from speak import speak,listen
import sqlite as sq

def firstWelcome():
	speak("hello sir , i am student assistant , i hope i will be helpful to you , i want to do some configuration , can you help me please ? ")
	speak("we will use the terminel to avoid mistakes !")
	speak("First ! can you entry your name , please ? ")
	print("your first name : ")
	fname = input()
	print("your last name : ")
	lname = input()
	speak("nice to meet you "+ fname)
	speak("how old are you "+ fname + " ? ")
	print("your age ? ")
	age = int(input())
	if age <= 18:
		speak(" what is your school name ?")
		print(fname + " entry your school name , please ?")
		schoolName = input()
	else :
		speak(fname + " what is your university name ?")
		print("entry your university name , please ?")
		univName = input()
		pass
	speak("what's year you are study in ? ")
	print("entry your degree ,please ?")
	degree = input()
	sq.create_connection(fname+lname+".sqlite")
	sq.create_student_table(fname+lname+".sqlite")
	sq.insertStudent(fname+lname+".sqlite",fname,lname,age,univName,degree)
	file = open("main.conf","w")
	file.write("dbname "+fname+lname+".sqlite")
	file.close()

def normalIntro():
	file = open("main.conf","r")
	dbs = file.readline()
	print(dbs)
	dbt = dbs.split(' ')
	print(dbt)
	dbname = ""
	if dbt[0] == "dbname":
		db = dbt[1]
	student = sq.select_student(db)
	speak("welcome back "+ student[1])
	
	