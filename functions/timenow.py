import time
from speak import speak 
def timenow():
	t = (time.ctime().split())[3].split(':')
	if t[1] == '00':
		speak(t[0] + "o'clock.")
	elif t[1] == '15':
		speak("quarter past "+t[0])
	elif t[1] == '30':
		speak("half past "+ t[0])
	elif t[1] == '45':
		speak("quarter to "+t[0])
	elif int(t[1]) < 30:
		speak(t[1] + " past " + t[0])
	elif int(t[1]) > 30:
		speak(t[1] + " to " + t[0])
	return ""
