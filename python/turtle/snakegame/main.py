import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('The Snake Game')
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()
game_on = True

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_one()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()