from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.goto(0, 350)
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score}', align='center', font=("Arial", 32, "normal"))

    def add_point(self):
        self.score += 1
        self.update_score()
