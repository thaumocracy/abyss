import random

PLAYER = 'X'
AI = "0"


CURRENT_PLAYER = PLAYER

INITIAL_FIELD = [
    ['•', '•', '•'],
    ['•', '•', '•'],
    ['•', '•', '•'],
]

field = [
    ['•', '•', '•'],
    ['•', '•', '•'],
    ['•', '•', '•'],
]


def print_field():
    print(field[0][0], field[0][1], field[0][2])
    print(field[1][0], field[1][1], field[1][2])
    print(field[2][0], field[2][1], field[2][2])


def check_input(x, y, current_player):
    if field[x][y] == '•' and not field[x][y] == current_player:
        return True
    return False


def check_win(current_player):
    row1 = (field[0][0] == current_player and field[0][1] ==
            current_player and field[0][2] == current_player)
    row2 = (field[1][0] == current_player and field[1][1] ==
            current_player and field[1][2] == current_player)
    row3 = (field[2][0] == current_player and field[2][1] ==
            current_player and field[2][2] == current_player)
    col1 = (field[0][0] == current_player and field[1][0] ==
            current_player and field[2][0] == current_player)
    col2 = (field[0][1] == current_player and field[1][1] ==
            current_player and field[2][1] == current_player)
    col3 = (field[0][2] == current_player and field[1][2] ==
            current_player and field[2][2] == current_player)
    dia1 = (field[0][0] == current_player and field[1][1] ==
            current_player and field[2][2] == current_player)
    dia2 = (field[0][2] == current_player and field[1][1] ==
            current_player and field[2][0] == current_player)
    if row1 or row2 or row3 or col1 or col2 or col3 or dia1 or dia2:
        print(f'Current player:{current_player} won!')
        return True
        print_field()


def make_input(x, y, current_player):
    if check_input(x, y, current_player):
        field[x][y] = current_player
        check_win(CURRENT_PLAYER)
    else:
        print('Your input is not correct, try again')
    print_field()


def get_input():
    global CURRENT_PLAYER
    user_input = input('Enter numbers:')
    nums = user_input.split()
    if nums[0].isdigit() and nums[1].isdigit():
        make_input(int(nums[0]), int(nums[1]), CURRENT_PLAYER)
        if CURRENT_PLAYER == PLAYER:
            CURRENT_PLAYER = AI
        else:
            CURRENT_PLAYER = PLAYER


def main():
    global CURRENT_PLAYER
    game_on = True
    while game_on:
        if check_win(CURRENT_PLAYER):
            game_on = False
            return
        get_input()


main()
