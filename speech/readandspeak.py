import pyttsx3
def speak(x):
    engine = pyttsx3.init() 
    engine.say(x)
    engine.runAndWait()
