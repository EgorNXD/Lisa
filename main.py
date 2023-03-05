import turtle
import turtle as t


t = turtle.Turtle()
t.speed(1)
def Triangle1(x,y,size,angle):
  t.up()
  t.color("orange")

  t.goto(x,y)
  t.right(angle)
  t.down()
  t.right(angle)
  t.forward(100*size)
  t.left(110)
  t.forward(146*size)
  t.left(140)
  t.forward(146*size)


  """
  Function draws Triangle1.
  """
  pass

# Triangle1(0,0,2,0)

def Circle(x,y, size, color):
  t.up()
  t.goto(x, y)
  t.color(color)
  t.down()

  t.circle(size)

  pass


Circle(0,0,100,"red")




