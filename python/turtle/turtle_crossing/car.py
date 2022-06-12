from turtle import Turtle


class Car(Turtle):
    def __init__(self, x_pos, y_pos, move_speed):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('blue')
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.goto(x_pos, y_pos)
        self.setheading(180)
        self.move_speed = move_speed

    def move(self):
        self.forward(self.move_speed)
        if self.xcor() < -500:
            self.goto(500, self.y_pos)
