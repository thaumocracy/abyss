from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = func(*args, **kwargs)
        time2 = time()
        print(f'Performance time is {time2 - time1}')
        return result
    return wrapper


@performance
def long_function():
    for i in range(10000000):
        i*5


long_function()
