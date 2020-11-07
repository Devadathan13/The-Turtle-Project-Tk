from tkinter import *
from PIL import ImageTk, Image
import os
import patterns
from script import CordParser
import turtle
from time import sleep
tk= Tk()
tk.title("The Turtle Project")
frame=Frame()
frame.pack()
from rand_gen import RandomArt
from tkinter import messagebox 


def pre_built():
	global frame
	global img
	frame.destroy()
	frame=Frame()
	frame.pack()
	img = ImageTk.PhotoImage(Image.open("t1.png"))
	panel = Label(frame, image = img)
	panel.pack(side= "top")
	pro= Button(frame, text="Protractor", command=patterns.protractor).pack()
	color= Button(frame, text="Colour Spiral", command=patterns.color_spiral).pack()
	worm= Button(frame, text="Worm hole", command=patterns.wormhole).pack()
	web= Button(frame, text="Spider Web", command=patterns.spider_web).pack()
	gamut= Button(frame, text="Color Gamut", command=patterns.color_gamut).pack()
	flower= Button(frame, text="Flowers", command=patterns.flowers).pack()
	modern= Button(frame, text="Modern Art", command=patterns.modern_art).pack()
	poly= Button(frame, text="Polygon", command=patterns.polygon).pack()
	back= Button(frame, text="Back", command=home, relief=GROOVE, bg="violet").pack(side="bottom", pady=10)


def read():
	def start():
		pattern = ".code"
		#try:
		while True:
			filename = str(entry.get())
			print(filename)
			if pattern==(filename[-5:-1]+"e"):
				t = turtle.Turtle()
				with CordParser(filename, "r") as par:
					sleep(1)
					count = 0
					
					for i in par:
						if i[count][0] == "f":
							t.fd(int(i[count][1]))
						if i[count][0] == "b":
							t.backward(int(i[count][1]))
						if i[count][0] == "l":
							t.left(int(i[count][1]))
						if i[count][0] == "r":
							t.right(int(i[count][1]))
						if i[count][0] == "u":
							t.penup()
						if i[count][0] == "d":
							t.pendown()

						count += 1
				turtle.mainloop()
				break

			else:
				messagebox.showerror("File Error", "Please use a valid '.code' file")
				break
		'''except:
			print("hi")
			pass'''
	global frame
	global img
	frame.destroy()
	frame=Frame()
	frame.pack()
	img = ImageTk.PhotoImage(Image.open("t1.png"))
	panel = Label(frame, image=img).pack()
	entry=Entry(frame)
	entry.pack()
	b5= Button(frame, text="Draw", command=start).pack()
	b6= Button(frame, text="Back", command=home, relief=GROOVE, bg="violet").pack(pady=20)


def home():
	global frame
	global img
	frame.destroy()
	frame=Frame()
	frame.pack()
	img = ImageTk.PhotoImage(Image.open("t1.png"))
	panel = Label(frame, image=img)
	panel.grid(row=0, column=1, columnspan=1)
	b1= Button(frame, text= "Custom Drawing", command=RandomArt.begin, relief=GROOVE, bg="violet").grid(row=1, column=0, columnspan=2, sticky=W, padx=200, pady=20)
	b2= Button(frame, text= "Pre-Built Patterns", command=pre_built, relief=GROOVE, bg="violet").grid(row=1, column=1, columnspan=3, sticky=E, padx=200, pady=20)
	b3= Button(frame, text="Import File", command=read, relief=GROOVE, bg="violet").grid(row=1,column=1 )


if __name__=="__main__":
	home()
tk.mainloop()