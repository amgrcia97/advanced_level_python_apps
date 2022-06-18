import pyttsx3

engine_obj = pyttsx3.init()

engine_obj.setProperty('rate', 150)
engine_obj.setProperty('voice', 'f1')

engine_obj.say('hello world')

engine_obj.runAndWait()
