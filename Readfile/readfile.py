from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pyttsx3
import sys
def read():
	Tk().withdraw() 
	filename = askopenfilename() 
	fi = open(filename,"r")
	msg = fi.read()
	engine = pyttsx3.init() 
	engine.say(msg)
	engine.runAndWait()
def stop():
	sys.exit()

