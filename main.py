import turtle
turtle.shape('turtle')
n=6
i=1
def tsvetok(i):
  while i<=n:
     turtle.circle(50)
     turtle.left(360/n)
     i=i+1
tsvetok(i)
