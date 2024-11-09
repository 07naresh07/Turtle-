import turtle
import random

t = turtle.Pen()
t.color('white')
t.speed(5)
colors = ['red', 'cyan', 'green', 'hotpink', 'gray', 'red']
def polygon(side):
    for i in range(0,4):
        t.forward(side)
        t.left(90)

for poly in range(10, 100, 10):
    random.shuffle(colors)
    t.color(colors[0])
    t.begin_fill()
    polygon(poly)
    t.end_fill()
    t.up()
    t.forward(10)
    t.right(20)
    t.down()

turtle.mainloop()
