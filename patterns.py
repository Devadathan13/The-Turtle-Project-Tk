import turtle
import random

def check():
	try:
		turtle.clearscreen()
	except:
		pass

def flowers():
	check()
	turtle.colormode(255)
	bob= turtle.Turtle()
	bob.speed(100)
	for n in range(60):
		bob.penup()
		bob.goto(random.randint(-700, 700), random.randint(-700, 700))
		bob.pendown()
		red_amount = random.randint(1, 255)  #/ 100.0
		blue_amount = random.randint(1, 255)  #/ 100.0
		green_amount = random.randint(1, 255)  # / 100.0
		bob.pencolor((red_amount, green_amount, blue_amount))
		circle_size = random.randint(10, 40)
		bob.pensize(random.randint(1, 5))
		for i in range(6):
			bob.circle(circle_size)
			bob.left(60)
	turtle.done()
#------------------------------------------------------------------------------------------------
def modern_art():
	check()
	bob= turtle.Turtle()
	n = 30    # number of stars 
	x = 144   # exterior angle of each star 
	angle = 40 
	bob.speed(70)
	for i in range(n):   
		turtle.colormode(255)  
		a = random.randint(0, 255) 
		b = random.randint(0, 255) 
		c = random.randint(0, 255) 
		bob.pencolor(a, b, c) 
		bob.fillcolor(a, b, c) 
		bob.begin_fill()  
		# loop for drawing each star 
		for j in range(5):  
			bob.forward(5 * n-5 * i) 
			bob.right(x) 
			bob.forward(5 * n-5 * i) 
			bob.right(72 - x) 	  
		# colour filling complete 
		bob.end_fill()   
		# rotating for 
		# the next star 
		bob.rt(angle) 
	turtle.done()
#--------------------------------------------------------------------------------------------------------------------
def polygon():
	check()
	bob= turtle.Turtle()
	bob.speed(0) # sets the speed of drawing to 0, which is the fastest
	bob.pencolor('white')
	turtle.bgcolor('black') 

	x = 0
	bob.up() # lifts up the pen, so no lines are drawn

	bob.rt(45) 
	bob.fd(90) 
	bob.rt(135) 

	bob.down()
	while x < 120:
		bob.fd(200)     
		bob.rt(61)
		bob.fd(200)
		bob.rt(61)
		bob.fd(200)
		bob.rt(61)
		bob.fd(200)
		bob.rt(61)
		bob.fd(200)
		bob.rt(61)
		bob.fd(200)
		bob.rt(61)

		bob.rt(11.1111) 
		x = x+1
	turtle.done()
#-----------------------------------------------------------------------------------------------------
def color_gamut():
	check()
	bob= turtle.Turtle()
	bob.speed(-1)
	turtle.reset()
	turtle.hideturtle()

	turtle.bgcolor('black')

	c = 0
	x = 0

	colors = [
	#reddish colors
	(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
	#orangey colors
	(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
	#yellowy colors
	(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
	#greenish colors
	(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
	#blueish colors
	(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
	]

	while x < 1000:
		idx = int(c)
		color = colors[idx]
		bob.color(color)
		bob.forward(x)
		bob.right(98)
		x = x + 1
		c = c + 0.1
	turtle.done()


def protractor():
	check()
	bob = turtle.Turtle()
	for angle in range(0, 360, 15):
		bob.setheading(angle)
		bob.forward(250)
		bob.write(str(angle) + '°')
		bob.backward(250)
	turtle.done()


def color_spiral():
	check()
	bob=turtle.Turtle()
	colors = ["red", 'purple', 'blue', 'green', 'yellow', 'orange']
	bob = turtle.Turtle()
	bob.speed(50)
	turtle.bgcolor("black")
	for x in range(360):
		bob.pencolor(colors[x % 6])
		bob.width(x / 100 + 1)
		bob.forward(x)
		bob.left(59)
	turtle.done()

def wormhole():
	check()
	bob = turtle.Turtle()
	bob.speed(100)
	turtle.bgcolor("black")
	bob.pencolor("white")
	for i in range(180):
		bob.forward(200)
		bob.right(30)
		bob.forward(20)
		bob.left(60)
		bob.forward(50)
		bob.right(30)
		bob.penup()
		bob.setposition(0, 0)
		bob.pendown()
		bob.right(2)
	turtle.done()
#-----------------------------------------------------------------------------------------------------
def spider_web():
	check()
	bob= turtle.Turtle()
	for i in range(6):
	   bob.forward(150)
	   bob.backward(150)
	   bob.right(60)

	side = 150
	for i in range(15):
	   bob.penup()
	   bob.goto(0,0)
	   bob.pendown()
	   bob.setheading(0)
	   bob.forward(side)
	   bob.right(120)
	   for j in range(6):
		   bob.forward(side)
		   bob.right(60)
	   side = side - 10
	turtle.done()