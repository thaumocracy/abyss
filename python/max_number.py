import random
data = []
maximum = 0

for item in range(50):
    data.append(random.randint(1, 100))

for item in data:
    if item > maximum:
        maximum = item


print(maximum)
