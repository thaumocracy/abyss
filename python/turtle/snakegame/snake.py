from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.moving_distance = 20
        self.head = self.segments[0]  # указатель на первый сегмент в списке - "голову" змеи

    def make_snake(self):
        for segment in range(0, 3):
            new_turtle = Turtle(shape='square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.goto(-(segment * 20), 0)
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(self.moving_distance)

    def extend(self):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(self.segments[-1].position())
        self.segments.append(new_turtle)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
