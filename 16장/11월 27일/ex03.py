import turtle

t = turtle.Pen()
t.speed(10)

t.reset()
for x in range(1, 38):
    t.left(175)
    t.forward(80)
    t.left(225)
    t.forward(80)

turtle.done()