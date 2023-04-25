from p5 import *

c = 4
n = 0
num_circles = 1000
init = 0

def settings():
    size(400, 400)


def setup():
    background(0)
    title("Sunflower Pattern")
    colorMode(HSB)


def draw():
    global n, num_circles, init

    if init == num_circles:
        saveCanvas("../images/phyllotaxis.png")
        exit()

    a = n * 137.5
    r = c * sqrt(n)

    x = r * cos(a) + 400 / 2
    y = r * sin(a) + 400 / 2

    ellipse(x, y, 4, 4)
    fill(n % 256, 255, 255)
    noStroke()

    n += 1
    init += 1


run()
