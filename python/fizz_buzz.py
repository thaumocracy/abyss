import random

for item in range(101):
    if item % 3 == 0 and item % 5 == 0:
        print('FizzBuzz', item)
    elif item % 3 == 0:
        print('Buzz', item)
    elif item % 5 == 0:
        print('Fizz', item)
    else:
        print(item)
