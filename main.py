#!/usr/bin/python

#Oussama Messabih
#email : giantscrusher@gmail.com

#Project : Student Assistant 

import speech_recognition
import pyttsx
from gtts import gTTS
import os

#speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
#rate = speech_engine.getProperty('rate')
#print('rate : ' , rate)
#speech_engine.setProperty('rate', rate)
#speech_engine.setProperty('gender','female')
#speech_engine.setProperty('age',25)
#voices = speech_engine.getProperty('voices')
#def Espeak(text)
	#speech_engine.setProperty('voice',voices[30])
	#speech_engine.say(text)
	#speech_engine.runAndWait()

def speak(text):

	tts = gTTS(text, lang='en')
	tts.save("text.mp3")
	os.system("mpg123 text.mp3")
	os.system("rm text.mp3")

recognizer = speech_recognition.Recognizer()

def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		# return recognizer.recognize_sphinx(audio)
		return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""
iamright = True 
speak("hey sam ! , how i can help you ? ")
while 1:
	speak("I heard you say " + listen())
	speak(" did i am right ? ")
	print("listen ... ")
	ans = listen()
	if ans == "yes":
		speak("i am very happy ")
	elif ans == "no":
		speak("i am very sorry ")
	elif ans == "":
		speak("no return")

