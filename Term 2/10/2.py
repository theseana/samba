import turtle as tr
import random as rnd

side = rnd.randint(10, 150)
tr.pensize(rnd.randint(1, 5))
tr.speed(1000)
for i in range(4):
    tr.forward(side)
    tr.left(90)

tr.done()
