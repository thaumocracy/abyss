calc_logo = """
 _____________________
|  _________________  |
| |              0. | |
| |___ ___ ___   ___| |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""


def main():
    print(calc_logo)
    working = True
    current_result = 0
    while working:
        if not current_result:
            n1 = float(input('Enter first number: \n'))
        else:
            n1 = current_result
        operand = input('Enter an operation or "c" to exit: \n')
        if operand == 'c':
            working = False
            return
        n2 = float(input('Enter the second number: \n'))
        if operand == '+':
            current_result = add(n1, n2)
            print(current_result)
            continue
        elif operand == '-':
            current_result = subtract(n1, n2)
            print(current_result)
            continue
        elif operand == '*':
            current_result = multiply(n1, n2)
            print(current_result)
            continue
        elif operand == '/':
            current_result = divide(n1, n2)
            print(current_result)
            continue


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


main()
