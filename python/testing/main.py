def do_stuff(number=0):
    try:
        if number:
            return int(number) + 5
        else:
            return 'Enter a number'
    except ValueError as error:
        return error
