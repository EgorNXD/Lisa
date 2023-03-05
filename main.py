"""
Salary:
"""

import turtle

t = turtle.Turtle()
t.speed(2)
t.pencolor("black")


#Main triangle
def Triangle(x,y,size,angle):
  t.up()
  t.fillcolor("orange")
  t.goto(x,y)
  t.right(angle)
  t.down()

  t.begin_fill()
  t.forward(100*size)
  t.left(110)
  t.forward(146.1902*size)
  t.left(140)
  t.forward(146.1902*size)
  t.seth(0)
  t.end_fill()
  """
  Draws triangle.
  x,y - start coordinates,
  size - size of the triangle
  angle - turning angle
  """
  pass


#Tail triangle
def Tail(x,y,size):
  t.up()
  t.fillcolor("orange")
  t.goto(x,y)
  t.down()

  t.begin_fill()
  t.left(90)
  t.forward(28.7939*size)
  t.right(100)
  t.forward(10*size)
  t.right(100)
  t.forward(28.7939*size)
  t.seth(0)
  t.end_fill()
  """
  Draws triangle-tail.
  x,y - start coordinates.
  size - size of the triangle.
  """
  pass


#Circle
def Circle(x,y, size, color):
  t.up()
  t.goto(x, y)
  t.fillcolor(color)
  t.down()

  t.begin_fill()
  t.circle(size)
  t.seth(0)
  t.end_fill()

  """
  Draws circle.
  x,y - start coordinates.
  size - size of the circle.
  color - color of filling.
  """
  pass


#Test zone
#Triangle(0,0,1,0)
#Tail(100,0,3)
#Circle(0,100,50,"red")

turtle.done()

