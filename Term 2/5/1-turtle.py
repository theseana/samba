import turtle as tr

s = input("Enter Shape(type 'square' or 'triangle'): ")
n = input("Enter Size")
n = int(n)
if s == 'square':
    tr.forward(n)
    tr.left(90)
    tr.forward(n)
    tr.left(90)
    tr.forward(n)
    tr.left(90)
    tr.forward(n)
    tr.left(90)
elif s == 'triangle':
    tr.forward(n)
    tr.left(120)
    tr.forward(n)
    tr.left(120)
    tr.forward(n)
    tr.left(120)

tr.done()
