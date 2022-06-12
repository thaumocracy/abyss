# import pandas
#
# data = pandas.read_csv('data.csv')
# dict_data = data.to_dict()
# print(dict_data)
# # temps = data['temp'].to_list()
# # print(sum(temps) / len(temps))
#
# print(data['temp'].max())
#
# import pandas
#
# data = pandas.read_csv('squirrels.csv')
# furs = data['Primary Fur Color'].value_counts()
#
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [furs.Gray, furs.Cinnamon, furs.Black]
# }
#
# print(data_dict)
#
# df = pandas.DataFrame(data_dict)
# df.to_csv('furs.csv')
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=750, height=500)
screen.bgpic('./states.gif')

states_data = pandas.read_csv('states.csv')
guessed_states = []
all_states = [item.lower() for item in states_data['state'].to_list()]

writer = Turtle()
writer.hideturtle()
writer.pencolor('red')
writer.penup()


def get_state(name):
    if name in all_states:
        item = states_data[states_data["state"] == name.title()]
        return [item['state'].item(), int(item['x']), int(item['y'])]
    else:
        return None


def check_state(name):
    if name.lower() in all_states and not name.lower() in guessed_states:
        return True
    else:
        return False


def open_state(state):
    print(state)
    writer.goto(state[1], state[2])
    writer.write(f"{state[0].title()}")


game_on = True

while game_on:
    if guessed_states == all_states:
        print('You won,amazing!')
        game_on = False
    user_input = screen.textinput(title='Guess a state', prompt='').lower()
    if get_state(user_input) and check_state(user_input):
        open_state(get_state(user_input))
        guessed_states.append(user_input)

screen.exitonclick()
