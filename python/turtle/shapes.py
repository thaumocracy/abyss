import turtle as t
import random
import colorgram

colors = colorgram.extract('./test.jpg', 5)
# print(colors[random.randint(0, len(colors) - 1)].rgb)


t.colormode(255)
knob = t.Turtle()
knob.shape('turtle')
knob.speed(0)


# colors = ['hotpink', 'khaki', 'firebrick', 'LimeGreen', 'navy', 'purple']


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def draw_square(side, turtle):
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)


def draw_circle(angle, size, turtle):
    turtle.pencolor(random_color())
    turtle.home()
    turtle.setheading(angle)
    turtle.circle(size)


def draw_shape(side, sides, turtle):
    turtle.color(random.choice(colors))
    angle = abs(360 / sides)
    for _ in range(sides):
        turtle.forward(side)
        turtle.right(angle)


def draw_dotted_line(size, length, turtle):
    for _ in range(length):
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
        turtle.forward(size)


def go_wild(turtle):
    turtle.pencolor(random_color())
    angles = [0, 90, 180, 270]
    turtle.left(random.choice(angles))
    turtle.forward(40)


def dot_line(turtle, amount, blank):
    turtle.penup()
    for _ in range(amount):
        turtle.dot(10, random_color())
        turtle.forward(blank)


# knob.pensize(10)
# for _ in range(50):
#     go_wild(knob)
#
# draw_square(50, knob)
# draw_square(150, knob)
#
# draw_dotted_line(30, 10, knob)
#
# draw_shape(100, 3, knob)
# draw_shape(100, 4, knob)
# draw_shape(100, 5, knob)
# draw_shape(100, 6, knob)
# draw_shape(100, 7, knob)
# draw_shape(100, 8, knob)
# draw_shape(100, 9, knob)
# draw_shape(100, 10, knob)
# draw_shape(100, 11, knob)
# draw_shape(100, 12, knob)
#
# for angle in range(0, 360, 5):
#     draw_circle(angle, 200, knob)

for rows in range(10):
    knob.pencolor(colors[random.randint(0, len(colors) - 1)].rgb)
    knob.setposition(0, rows * 30)
    dot_line(knob, 10, 30)

screen = t.Screen()
screen.exitonclick()
