# square the array using lambda func
array = [1, 2, 3, 4, 5, 6]

print(list(map(lambda item: item ** 2, array)))

# Sort array by 2nd item in tuple

tuple_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
tuple_list.sort(key=lambda item: item[1])
print(tuple_list)
