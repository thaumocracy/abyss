import random
data = []
summ = 0

for item in range(50):
    data.append(random.randint(1, 100))

for item in data:
    if item % 2 == 0:
        summ += item


print(summ)
