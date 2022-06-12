import random
import sys


def getPoint(start=1, stop=10):
    return random.randrange(start, stop)


def genStart(number=0):
    try:
        if number:
            return int(number)
        else:
            return 'Enter a valid start number'
    except:
        print('Start has an error')


def genStop(number=10):
    try:
        if number:
            return int(number)
        else:
            return 'Enter a valid stop number'
    except:
        print('Stop has an error')


def checkAnswer(start, number, stop):
    return start <= number <= stop


def checkGuessed(guess, number):
    return guess == number


start = genStart(1)
stop = genStop(10)
point = getPoint(start, stop)

while True:
    print(point)
    try:
        guess = int(
            input(f'Guess a number between {start} and {stop} \n'))
        if checkAnswer(start, guess, stop):
            if checkGuessed(guess, point):
                print(f'YOU GUESSED RIGHT,FELLA! ITS {point}')
                break
    except ValueError:
        print(
            f'Hey,lets stick to numbers between {start} and {stop}')
