from random import randint, uniform
import turtle

number_of_turtles = 50
steps_of_time_number = 300

turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
turtle.penup()
turtle.goto(-350, -350)
turtle.pendown()
turtle.pensize(5)
turtle.goto(-350, 350)
turtle.goto(350, 350)
turtle.goto(350, -350)
turtle.goto(-350, -350)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.shapesize(0.5, 0.5)
    unit.vx = uniform(-1, 1) * 4
    unit.vy = uniform(-1, 1) * 4
    unit.penup()
    unit.speed(300)
    unit.goto(randint(-330, 330), randint(-330, 330))

for i in range(steps_of_time_number):
    for unit in pool:
        x = unit.xcor() + unit.vx
        y = unit.ycor() + unit.vy
        unit.goto(x, y)
        if unit.xcor() <= -330:
            unit.vx = -unit.vx
        if unit.ycor() <= -330:
            unit.vy = -unit.vy
        if unit.xcor() >= 330:
            unit.vx = -unit.vx
        if unit.ycor() >= 330:
            unit.vy = -unit.vy
