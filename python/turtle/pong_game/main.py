from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time

screen = Screen()

screen.setup(height=600, width=1000)
screen.bgcolor('black')
screen.title('The Pong Game')
screen.tracer(0)

right_paddle = Paddle((400, 0))
left_paddle = Paddle((-400, 0))
ball = Ball()
screen.listen()
scoreboard = Scoreboard()
screen.onkeypress(right_paddle.upwards, "Up")
screen.onkeypress(right_paddle.downwards, "Down")
screen.onkeypress(left_paddle.upwards, "w")
screen.onkeypress(left_paddle.downwards, "s")
# screen.onkeypress(ball.move, "r")
game_on = True

while game_on:
    if ball.xcor() > 500:
        ball.new_ball()
        scoreboard.l_point()
    if ball.xcor() < -500:
        ball.new_ball()
        scoreboard.r_point()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    time.sleep(0.1)
    ball.move()
    # Detect right paddle hit
    if ball.xcor() >= 380 and right_paddle.distance(ball) < 50 or ball.xcor() <= -380 and left_paddle.distance(
            ball) < 50:
        print('Hit achieved')
        ball.bounce_x()
        # ball.go_fast()
    screen.update()

screen.exitonclick()
