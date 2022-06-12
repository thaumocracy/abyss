from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.refresh()

    def add_one(self):
        self.clear()
        self.count += 1
        self.refresh()

    def refresh(self):
        string = f"Score = {self.count}"
        self.write(string, move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)