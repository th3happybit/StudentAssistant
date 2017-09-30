import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
	with sr.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
	try:
		# return recognizer.recognize_sphinx(audio)
		return recognizer.recognize_google(audio)
	except sr.UnknownValueError as e:
		print("Could not understand audio".format(e))
	except sr.RequestError as e:
		print("Recog Error; {0}".format(e))
	return ""
print(listen())
	