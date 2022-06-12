from turtle import Turtle

DISTANCE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.color('green')
        self.penup()
        self.goto(0, -100)

    def move(self):
        self.forward(DISTANCE)

    def restart(self):
        self.goto(0, -100)
