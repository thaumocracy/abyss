def highest_even(array):
    answer: int = 0
    for item in array:
        if item % 2 == 0 and item > answer:
            answer = item
    return answer


print(highest_even([1, 3, 4, 5, 6, 7, 8, 11, 12, 33, 44, 67, 91, 100]))
