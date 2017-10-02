from speak import speak
from listen import listen
import sqlite as sq
import configparser
config = configparser.ConfigParser()

def firstWelcome():
	speak("Hello sir , i am student assistant , i hope i will be helpful to you , i want to do some configuration , can you help me please ? ")
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
	speak("what do you want to name me ?")
	vsname = input()
	speak("Thank you "+fname+" I hope i will be hopeful to you ")
	sq.create_connection(fname+lname+".sqlite")
	sq.create_student_table(fname+lname+".sqlite")
	sq.insertStudent(fname+lname+".sqlite",fname,lname,age,univName,degree)
	cfg = open("main.cfg","w")
	config.add_section('database')
	config.set('database','dbname',fname+lname+".sqlite")
	config.add_section('assistantInfo')
	config.set('assistantInfo','name',vsname)
	config.write(cfg)
	cfg.close()

def normalIntro():
	config.read("main.cfg")
	db = ""
	if 'database' in config:
		db = config['database']['dbname']
	student = sq.select_student(db)
	speak("welcome back "+ student[1])

	