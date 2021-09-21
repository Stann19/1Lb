import turtle
from math import sin, pi
turtle.shape('turtle')
R =15
x = 1
n = 3
turtle.up()
turtle.goto(R, 0)
turtle.down()
def mng(x):
  while x <= n:
        turtle.left((180 - 360 /n)/2)
        turtle.left(360/n)
        turtle.forward(2 * R * sin(pi/n))
        x=x+1
        turtle.right((180-360/n)/2)
while n <= 12:
    mng(x)
    n=n+1
    R=R+35
    turtle.up()
    turtle.goto(R, 0)
    turtle.down()
