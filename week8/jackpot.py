'''
This program will develop a simple slot machine game.
1. draw 3 'slots' (squares) in a horizontal row
2. draw a 'Play' button below the slots
3. When the user clicks the Play button, display a randomly-chosen shape in each slot, choosing from these - square, circle, triangle
4. Fill each shape with a color - it's ok to hard-code one color per shape
5. If all 3 slots show the same shape, display a 'Winner!' message below the Play button
Gene Rocha
11/27/2019
'''
from graphics import *
import random

win = GraphWin("Slot Machine",600,600)

slot1 =  Rectangle(Point(10,10), Point(180,180))
slot2 =  Rectangle(Point(200,10), Point(380,180))
slot3 =  Rectangle(Point(400,10), Point(580,180))

playBtn =  Rectangle(Point(200,300), Point(380,380))

label = Text(Point(285,342), "Spin!")
label.setSize(20)

winner = Text(Point(285,453), "Winner!")
winner.setSize(30)
winner.setFill("Red")
# draw the graphics window, slots and labels
slot1.draw(win)
slot2.draw(win)
slot3.draw(win)
playBtn.draw(win)
label.draw(win)
# upper left and lower right of the play button
lx = range(200,380)
rx = range(300,380)
# add lists for slots and colors
slots = [slot1,slot2,slot3]
colors = ["Yellow","Blue","Red","Green","Black","Brown","Azure","Ivory","Teal","Silver","Purple","Navy blue","Gray","Orange","Maroon","Aquamarine","Coral","Fuchsia","Wheat","Lime","Crimson","Khaki","Hot pink","Magenta","Plum","Olive","Cyan"]

# circle function and pass the parameter slot
def circle(slot):
  aCircle = Circle(slot.getCenter(), 75)
  color = random.choice(colors)
  aCircle.setFill(color)
  aCircle.draw(win)
  return aCircle

# square function and pass the parameter slot
def square(slot):
  p1 = Point(slot.p1.getX() +20, slot.p1.getY() +20)
  p2 = Point(slot.p2.getX() -20,slot.p2.getY() -20)
  aSquare =  Rectangle(p1,p2)
  color = random.choice(colors)
  aSquare.setFill(color)
  aSquare.draw(win)
  return aSquare

# triangle function and pass the parameter slot
def triangle(slot):
  p1 = Point(slot.p1.getX() +20, slot.p2.getY() -20)
  p2 = Point(slot.p2.getX() -20,slot.p2.getY() -20)
  p3 = Point(slot.getCenter().getX(),slot.p1.getY() +20)
  aPolygon = Polygon(p1,p3,p2)
  color = random.choice(colors)
  aPolygon.setFill(color)
  aPolygon.draw(win)
  return aPolygon

# add the list for shapes
shapes =[]
while True:
  p = win.getMouse()
  if p.getX() in lx and p.getY() in rx:
      i = 0
      for s in shapes:
        s.undraw() # Remove the pervious shapes from the graphics window
      shapes.clear() # clear the pervious shapes from the list
      for i in slots:
        num = random.randrange(3) # set a random num
        if num == 0:
          shape = circle(i) # invoke the circle function and pass the slot num
        elif num == 1:
          shape = square(i) # invoke the square function and pass the slot num
        else:
          shape = triangle(i) # invoke the triangle function and pass the slot num
        shapes.append(shape)
      winner.undraw() # remove the winner label
      if type(shapes[0]) == type(shapes[1]) == type(shapes[2]):
        winner.draw(win) # draw the winner label
    # code that should execute with each mouse click should be here
win.mainloop() # this keeps the graphics window open on vs code