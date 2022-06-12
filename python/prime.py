def check_prime(num):
    counter = num - 1
    while counter >= 2:
        if num % counter == 0:
            print('Not prime')
            return
        counter -= 1
    print('Prime')


check_prime(17)
