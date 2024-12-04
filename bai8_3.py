import turtle
import random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

painter = turtle.Turtle()
painter.pensize(3)


for i in range(12):  
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)  

turtle.done()
