import turtle
turtle.shape('turtle')
i=1
n=50
turtle.left(90)
def baterfly(i):
  turtle.circle(n)
  turtle.circle(-n)
while i<=10:
  baterfly(i)
  n=n+5
  i=i+1



