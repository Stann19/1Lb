import turtle
from random import*
turtle.shape('turtle')
turtle.speed(10)
i=1
while i<=30:
    x=randint(0, 360)
    y=randint(0,70)
    turtle.forward(y)
    turtle.left(x)
    i=i+1

