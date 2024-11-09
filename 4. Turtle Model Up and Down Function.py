import turtle

t = turtle.Pen()
t.speed(5)

def Poly(side):
    for i in range(4):
        t.forward(side)
        t.left(90)

for poly in range(10, 100, 10):
    Poly(poly)

def Circle(radius):
    t.circle(radius)

for circ in range(10, 100, 10):
    Circle(circ)


turtle.mainloop()