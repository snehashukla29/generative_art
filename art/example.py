from p5 import *


def setup():
    size(200, 200)


def draw():
    rect_mode(CENTER)
    rect((100, 100), 20, 100)
    ellipse((100, 70), 60, 60)
    ellipse((81, 70), 16, 32)
    ellipse((119, 70), 16, 32)
    line((90, 150), (80, 160))
    line((110, 150), (120, 160))


run()