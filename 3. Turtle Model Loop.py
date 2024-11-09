import turtle
screen = turtle.Screen()
screen.title('Loop')
screen.bgcolor('hotpink')
t = turtle.Turtle()
t.shape('turtle')
t.color('green')
t.speed(5)

for i in range(0, 20):
    t.forward(50)
    t.left(95)

t.reset()       #Resets the loop data and to set the new data
t.penup()
t.forward(100)
t.pendown()
t.color('red')
for i in range(0,10):
    t.forward(50)
    t.right(135)

screen.mainloop()