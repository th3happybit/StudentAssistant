from speak import speak
from listen import listen
import sqlite as sq
import configparser
config = configparser.ConfigParser()

def firstWelcome():
	ask("Welcome to Student assistant , i hope i will be helpful to you , i want to do some configuration , can you help me please ? ")
	ask("we will use the terminel to avoid mistakes !")	
	ask("First ! can you entry your name , please ? ")
	fname = input()
	print("your last name : ")
	lname = input()
	ask("nice to meet you "+ fname)
	ask("how old are you "+ fname + " ? ")
	age = int(input())
	if age <= 18:
		ask(" what is your school name " + fname + " ?")
		schoolName = input()
	else :
		ask(" what is your university name "+fname+" ?")
		univName = input()
	ask("what's year you are study in ? ")
	print("ex : cpi2")
	degree = input()
	ask("what is your group ? ")
	print("ex : g1")
	gr = input()
	speak("what do you want to name me ?")
	vsname = input()
	speak("Thank you "+fname+" Enjoy !")
	sq.create_connection(fname+lname+".sqlite")
	sq.create_student_table(fname+lname+".sqlite")
	sq.insertStudent(fname+lname+".sqlite",fname,lname,age,univName,degree)
	cfg = open("data/main.cfg","w")
	config.add_section('database')
	config.set('database','dbname',fname+lname+".sqlite")
	config.add_section('assistantInfo')
	config.set('assistantInfo','name',vsname)
	config.add_section('user')
	config.set('user','firstname',fname)
	config.set('user','lastname',lname)
	config.set('user','degree',degree)
	config.set('user','group',gr)
	config.write(cfg)
	cfg.close()

def normalIntro():
	config.read("data/main.cfg")
	db = ""
	if 'database' in config:
		db = config['database']['dbname']
	student = sq.select_student(db)
	speak("welcome back "+ student[1])

def ask(text):
	speak(text)
	print(text)	