from tkinter import *
from tkinter import ttk
import random
import time
import tkinter.messagebox as msg
root = Tk()
f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()
f3 = Frame(root)
f3.pack()
f4 = Frame(root)
f4.pack()
f5 = Frame(root)
f5.pack()
f6 = Frame(root)
f6.pack()
f7 = Frame(root)
f7.pack()
root.geometry("700x700")
var = IntVar()
Title = Label(f1, text = 'Welcome to Trivia', fg = 'green', font = ('arial',15, 'bold')).pack()
questions = [1,2,3,4,5,6]

def j():
	t = var.get()
	if t == 1:
		msg.showinfo('','Wrong')
	elif t == 2:
		msg.showinfo('','Correct')
	elif t == 3:
		msg.showinfo('','Wrong')
	f5.destroy()
	question5()
	f6.pack()



def k():
	t = var.get()
	if t == 1:
		msg.showinfo('','Correct')
	elif t == 2:
		msg.showinfo('','Wrong')
	elif t == 3:
		msg.showinfo('','Wrong')
	f2.destroy()
	question2()
	f3.pack()



def h():
	t = var.get()
	if t == 1:
		msg.showinfo('','Wrong')
	elif t == 2:
		msg.showinfo('','Correct')
	elif t == 3:
		msg.showinfo('','Wrong')
	f3.destroy()
	question3()
	f4.pack()
def question1():
	lbl = Label(f2, text = 'Question: Which African country was formerly known as Abyssinia?', fg = 'green', font = ('arial',15, 'bold'))
	lbl.pack()
	b1 = Radiobutton(f2, text = 'Ethiopia', variable = var, value = 1, command = k)
	b1.pack()
	b2 = Radiobutton(f2, text = 'Seychelles', variable = var, value = 2, command = k)
	b2.pack()
	b3 = Radiobutton(f2, text = 'Djibouti', variable = var, value = 3, command = k)
	b3.pack()


def question4():
	lbl = Label(f5, text = 'Question: What’s the heaviest organ in the human body?', fg = 'green', font = ('arial',15, 'bold'))
	lbl.pack()
	b1 = Radiobutton(f5, text = 'Brain', variable = var, value = 1, command = j)
	b1.pack()
	b2 = Radiobutton(f5, text = 'Liver', variable = var, value = 2, command = j)
	b2.pack()
	b3 = Radiobutton(f5, text = 'Heart', variable = var, value = 3, command = j)
	b3.pack()

def l():
	t = var.get()
	if t == 1:
		msg.showinfo('','Wrong')
	elif t == 2:
		msg.showinfo('','Wrong')
	elif t == 3:
		msg.showinfo('','Correct')
	f6.destroy()
	question6()
	f7.pack()
def question5():
	lbl = Label(f6, text = 'Question: What is the only food that cannot go bad?', fg = 'green', font = ('arial',15, 'bold'))
	lbl.pack()
	b1 = Radiobutton(f6, text = 'Dark chocolate', variable = var, value = 1, command = l)
	b1.pack()
	b2 = Radiobutton(f6, text = 'Canned tuna', variable = var, value = 2, command = l)
	b2.pack()
	b3 = Radiobutton(f6, text = 'Honey', variable = var, value = 3, command = l)
	b3.pack()




def question2():
	lbl = Label(f3, text = 'Question: What year did the Berlin wall fall?', fg = 'green', font = ('arial',15, 'bold'))
	lbl.pack()
	b1 = Radiobutton(f3, text = '1981', variable = var, value = 1, command = h)
	b1.pack()
	b2 = Radiobutton(f3, text = '1989', variable = var, value = 2, command = h)
	b2.pack()
	b3 = Radiobutton(f3, text = '1985', variable = var, value = 3, command = h)
	b3.pack()
	
def i():
	t = var.get()
	if t == 1:
		msg.showinfo('','Correct')
	elif t == 2:
		msg.showinfo('','Wrong')
	elif t == 3:
		msg.showinfo('','Wrong')
	f4.destroy()
	question4()
	f5.pack()
def question3():
	lbl = Label(f4, text = 'Question: What type of food holds the world record for being the most stolen around the globe?', fg = 'green', font = ('arial',15, 'bold'))
	lbl.pack()
	b1 = Radiobutton(f4, text = 'Cheese', variable = var, value = 1, command = i)
	b1.pack()
	b2 = Radiobutton(f4, text = 'Chocolate', variable = var, value = 2, command = i)
	b2.pack()
	b3 = Radiobutton(f4, text = 'Wagyu beef', variable = var, value = 3, command = i)
	b3.pack()
def o():
	t = var.get()
	if t == 1:
		msg.showinfo('','Wrong')
	elif t == 2:
		msg.showinfo('','Wrong')
	elif t == 3:
		msg.showinfo('','Correct')
	root.destory()
def question6():
	lbl = Label(f7, text = 'Question: Which fast food restaurant has the largest number of retail locations in the world?', fg = 'green', font = ('arial',15, 'bold'))
	lbl.pack()
	b1 = Radiobutton(f7, text = 'Chipotle', variable = var, value = 1, command = o)
	b1.pack()
	b2 = Radiobutton(f7, text = "McDonald’s", variable = var, value = 2, command = o)
	b2.pack()
	b3 = Radiobutton(f7, text = 'Subway', variable = var, value = 3, command = o)
	b3.pack()





def Clickme():
	f1.destroy()
	question1()
b1 = Button(f1, text = 'Enter', command = Clickme)
b1.pack()

mainloop()

