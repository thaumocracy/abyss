from turtle import Turtle, Screen

knob = Turtle()
screen = Screen()


def move_forwards():
    knob.forward(30)


def move_backwards():
    knob.backward(30)


def turn_left():
    knob.left(10)


def turn_right():
    knob.right(10)


def clear():
    knob.home()
    knob.clear()


screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
