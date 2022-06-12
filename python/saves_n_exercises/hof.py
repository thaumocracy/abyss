from functools import reduce

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# example array
zipList = [10, 20, 30, 40, 50]


def multiply_by_2(num):
    return num * 2


print(list(map(multiply_by_2, array)))


def check_even(num):
    return num % 2 == 0


print(list(filter(check_even, array)))


print(list(zip(array, zipList)))


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, array, 0))
