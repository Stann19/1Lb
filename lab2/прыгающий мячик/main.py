import turtle
turtle.shape('circle')
turtle.shapesize(0.5)
turtle.speed(10)
g=9.8
vx=60
vy=120
x=0
y=0
count=0
n=0.005
for i in range(1000):
    if y<=0:
        vy=abs(vy)
        count+=1
    vx-=n*vx
    vy-=n*vy
    x+=vx*i/5000
    y+=vy*i/5000-g*((i/5000)**2)/2
    turtle.goto(x, y)
    vy-=g*i/5000
