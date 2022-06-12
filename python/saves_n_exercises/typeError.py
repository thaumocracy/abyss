def sum(num1, num2):
    try:
        return num1+num2
    except TypeError as err:
        print(err)


sum(1, '2')
