import time
import schelude as sch 
def timenow():
	t = (time.ctime().split())[3].split(':')
	if t[1] == '00':
		return t[0] + "o'clock."
	elif t[1] == '15':
		return "quarter past "+t[0]
	elif t[1] == '30':
		return "half past "+ t[0]
	elif t[1] == '45':
		return "quarter to "+t[0]
	elif int(t[1]) < 30:
		return t[1] + " past " + t[0]
	elif int(t[1]) > 30:
		return t[1] + " to " + t[0]  
	return ""

def schoolSchedule(cmd):
	if cmd == "":
		pass
	return
def search(subject):
	return
def openlink(link):
	return
def calcule(expr):
	return
def facebook():
	return
