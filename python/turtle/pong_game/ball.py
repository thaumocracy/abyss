from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.x_speed = 5
        self.speed(self.x_speed)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # def go_fast(self):
    #     self.x_speed += 1
    #     self.speed(self.x_speed)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def new_ball(self):
        self.home()
        self.bounce_x()