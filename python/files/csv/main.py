import csv
# data = []
# with open('data.csv', 'r') as file:
#     weather = file.readlines()
#     for day in weather[1:]:
#         arr = day.split(',')
#         new_day = [arr[0], arr[1], arr[2].strip()]
#         data.append(new_day)

# for item in data:
#     print(f"On {item[0]} was {item[1]} degrees C and quite a bit of {item[2]}")

with open('data.csv') as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(row[1])
    print(temperatures)
