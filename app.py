import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
""" 
t.forward(200) """

def message(input):
    print(input)
message("Hello Class")

message.done = True


""" def add(x,y)
    #variables here only accesible on the function, SCOPE
    return x + y
#call the function
z=add(5,15) """

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200) """


""" def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200)  """

""" def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right() """

def rectangle(x):
    t.forward(x)
    t.left(100)
    t.forward(x/2)
    t.left(125)
    t.forward(x)
    t.left(100)
    t.forward(x/2)
    t.left(125)
rectangle(200)