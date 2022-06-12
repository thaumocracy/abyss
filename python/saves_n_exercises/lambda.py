array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mapped_array = list(map(lambda item: item * 2, array))
filtered_array = list(filter(lambda item: item % 2 is 0, array))

print(array)
print(mapped_array)
print(filtered_array)
