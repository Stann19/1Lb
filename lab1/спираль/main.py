import turtle
from math import sin, cos, pi
turtle.shape('turtle')
i=0
while i<=360:
    x=i/5*cos(i/5)
    y=i/5*sin(i/5)
    turtle.goto(x,y)
    i=i+1
