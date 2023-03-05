import turtle
import turtle as t


t = turtle.Turtle()
t.speed(1)
t.pencolor("black")

def Triangle1(x,y,size,angle):
  t.up()
  t.fillcolor("orange")
  t.goto(x,y)
  t.right(angle)
  t.down()
  t.begin_fill()
  t.forward(100*size)
  t.left(110)
  t.forward(146*size)
  t.left(140)
  t.forward(146*size)
  t.end_fill()


  """
  Function draws Triangle1.
  """
  pass

#Triangle1(0,0,2,0)

def Triangle2(x,y,size):
  t.up()
  t.fillcolor("orange")
  t.goto(x,y)
  t.left(90)
  t.down()
  t.begin_fill()
  t.forward(100*size)
  t.right(100)
  t.forward(10*size)
  t.right(85)
  t.forward(100*size)
  t.end_fill()
  pass
Triangle2(0,0,2)

def Circle(x,y, size, color):
  t.up()
  t.goto(x, y)
  t.fillcolor(color)
  t.down()
  t.begin_fill()
  t.circle(size)
  t.end_fill()

  pass


# Circle(0,0,100,"red")





