from gtts import gTTS
import os

def speak(text):
	tts = gTTS(text, lang='en')
	tts.save("text.mp3")
	os.system("mpg123 text.mp3")
	os.system("rm text.mp3")

