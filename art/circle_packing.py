import random
from p5 import * 

create_circle_attempts = 500
num_circles = 500
min_radius = 2
max_radius = 100

canvas_h = 640
canvas_w = 360

all_circles = []


def setup():
    global canvas_h, canvas_w
    size(canvas_h, canvas_w)
    background(110)
    fill(0, 110)


def draw():
    global num_circles, all_circles

    ellipseMode(RADIUS)
    fill(255)

    for attempt in range(0, num_circles):
        create_circle()

    for c in all_circles:
        ellipse(c.x, c.y, c.r, c.r)

    noLoop()
    # save_frame("firstRun.png")


def does_circle_have_collision(current_circle):

    for c in all_circles:
        a = c.r + current_circle.r
        x = current_circle.x - c.x
        y = current_circle.y - c.y

        # if dist((current_circle.x, current_circle.y), (x, y)) < a:
        if math.sqrt((x*x) + (y*y)) < a:
            return True

    return False


def create_circle():
    global min_radius, canvas_h, canvas_w, min_radius, max_radius, all_circles, create_circle_attempts

    circle_safe = False
    new_circle = None

    for x in range(0, create_circle_attempts):

        x_coord = random.randint(0, canvas_h)
        y_coord = random.randint(0, canvas_w)

        new_circle = Circle(x_coord, y_coord, min_radius)

        circle_safe = not does_circle_have_collision(new_circle)

    if not circle_safe:
        return

    for i in range(min_radius, max_radius):
        new_circle.r = i
        if does_circle_have_collision(new_circle):
            new_circle.r -= 1
            break

    all_circles.append(new_circle)


class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


run()
