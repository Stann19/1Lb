import turtle
turtle.shape('turtle')
i=1
n=5
turtle.right(180)
def star(n,i):
    turtle.left(180-180/n)
    turtle.forward(100)
while i<=n:
    star(n, i)
    i=i+1
