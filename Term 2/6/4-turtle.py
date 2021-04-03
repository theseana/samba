import turtle as tr

s = input("Enter Shape(type 'square' or 'triangle'): ")
n = input("Enter Size")
n = int(n)
i = 0

if s == 'square':
    while i < 4:
        tr.forward(n)
        tr.left(90)
        i += 1    
elif s == 'triangle':
    while i < 3:
        tr.forward(n)
        tr.left(120)
        i += 1
        
tr.done()