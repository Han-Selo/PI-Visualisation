import turtle as tu
import random

lines = 1000000
tu.screensize(3000, 3000, "black")

with open("PiVisualisierung\millionDigitsOfPi.txt", "r") as f:
    pi = f.read()
    

tu.mode("logo")
tu.tracer(False)
tu.colormode(255)
for n in range(lines):
    color = int(n/(lines/255))
    tu.pencolor(255, 255-color, color)
    zahl = int(pi[n])
    winkel = zahl*36
    tu.seth(0)
    
    tu.right(winkel)
    tu.forward(2)
    if n % 10000 == 0:
        tu.update()

    tu.left(winkel)

tu.getcanvas().postscript(file="PI_picture.eps")
tu.done()
