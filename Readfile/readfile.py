from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pyttsx3
import sys
import multiprocessing
def rea(msg):
	
	engine = pyttsx3.init() 
	engine.say(msg)
	engine.runAndWait()
def read1():
	Tk().withdraw() 
	filename = askopenfilename() 
	fi = open(filename,"r")
	msg = fi.read()
	global p1
	p1=multiprocessing.Process(name="p1",target=rea,args=(msg,))
	p1.start()
def stop():
	p1.terminate()
#read1()

