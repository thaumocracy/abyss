import random
import time
from turtle import Screen

from car import Car
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=800, width=1000)
screen.bgcolor('white')
screen.title('Turtle vs Cars')
screen.tracer(0)
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def create_cars():
    cars_arr = []
    for _ in range(0, 10):
        y_pos = _ * 30
        speed = random.randint(0, 15)
        create_car_row(cars_arr, speed, y_pos)
    return cars_arr


def create_car_row(cars_arr, speed, y_pos):
    for _ in range(0, random.randint(0, 10)):
        new_car = Car(600 + (random.randint(0, _) * random.randint(25, 50)), y_pos, speed)
        new_car.color(random_color())
        cars_arr.append(new_car)


cars = create_cars()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")
game_on = True
game_speed = 0.1
player_lives = 3
while game_on:
    time.sleep(game_speed)
    for car in cars:
        car.move()
        if player.distance(car) < 20:
            if player_lives <= 0:
                print('Game over')
                game_on = False
            player.restart()
            player_lives -= 1
        if player.ycor() > 350:
            scoreboard.add_point()
            game_speed *= 0.70
            player.restart()
    screen.update()

screen.exitonclick()
