from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.left(90)
        self.penup()
        self.speed(5)
        self.goto(coordinates)
        self.turtlesize(stretch_wid=1, stretch_len=5)

    def upwards(self):
        if 240 > self.ycor():
            self.forward(10)

    def downwards(self):
        if -240 < self.ycor():
            self.backward(10)
