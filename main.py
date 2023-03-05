"""
Salary:
"""

import turtle

t = turtle.Turtle()
t.speed(2)
t.width(2)
t.pencolor("black")


#Main triangle
def Triangle(x, y, size, angle):
  t.up()
  t.fillcolor("orange")
  t.goto(x, y)
  t.right(angle)
  t.down()
  t.begin_fill()
  t.forward(100*size)
  t.left(110)
  t.forward(146.1902*size)
  t.left(140)
  t.forward(146.1902*size)
  t.end_fill()
  t.seth(0)

  """
  Draws triangle.
  x,y - start coordinates,
  size - size of the triangle
  angle - turning angle
  """
  pass


#Tail triangle
def Tail(x, y, size):
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
  t.end_fill()
  t.seth(0)

  """
  Draws triangle-tail.
  x, y - start coordinates.
  size - size of the triangle.
  """
  pass


#Circle
def Circle(x, y, size, color):
  t.up()
  t.goto(x, y)
  t.fillcolor(color)
  t.down()
  t.begin_fill()
  t.circle(size)
  t.end_fill()
  t.seth(0)

  """
  Draws circle.
  x,y - start coordinates.
  size - size of the radius of the circle.
  color - color of filling.
  """
  pass

#Half Circle
def Smile(x, y, size, width):
  t.up()
  t.goto(x, y)
  t.pencolor("red")
  t.down()
  t.left(90)
  t.width(width)
  t.circle(size, -180)
  t.width(2)
  t.pencolor("black")
  t.seth(0)

  """
  Draws half circle.
  x,y - start coordinates.
  size - size of radius of the half circle.
  color - color of filling.
  """
  pass

#Rectangle
def Rec(x, y, a, b, color):
  t.up()
  t.goto(x, y)
  t.fillcolor(color)
  t.down()
  t.begin_fill()
  for i in range(2):
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(90)
  t.end_fill()
  t.seth(0)
  """
  Draws rectangle.
  x,y - start coordinates.
  a,b - sides length.
  color - color of filling.
  """
  pass



#Test zone
#Triangle(0,0,1,0)
#Tail(100,0,3)
#Smile(0,0,100,5)
#Circle(0,50,50,"red")
#Rec(0,0,100,50,"yellow")
turtle.done()
