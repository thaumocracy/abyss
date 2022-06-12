import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


playing = True
target = random.randint(0, 100)
attempts = 0

print(logo)
print("I'm thinking about number from 1 to 100")
print("Choose a difficulty. Type 'easy' or 'hard")
diff_input = input()

if diff_input == 'hard':
    attempts = 5
else:
    attempts = 10


def check_number(target, num):
    if target == num:
        return True
    elif num > target:
        print('Too high')
        return False
    elif num < target:
        print('Too low')
        return False


def main(attempts, target):
    while attempts > 0:
        guess = int(input('Guess a number:'))
        if check_number(target, guess):
            print('You guessed correct!')
            playing = False
            return
        else:
            attempts -= 1
            print(f'You have {attempts} left')
            print('--------------------------')
            continue


main(attempts, target)
