while True:
    try:
        age = int(input('Input ? \n'))
        print(10/age)
    except ValueError:
        print('Please enter correct number')
    except ZeroDivisionError:
        print('Please number higher than 0')
    else:
        break
