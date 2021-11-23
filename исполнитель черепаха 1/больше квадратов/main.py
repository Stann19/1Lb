import turtle
a=20
i=1
turtle.shape('turtle')
while i<=10:
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.right(45)
    turtle.penup()
    turtle.forward(14)
    turtle.left(135)
    turtle.pendown()
    a=a+20
    i=i+1

