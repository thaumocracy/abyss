# import random
#
# names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
#
# new_list = {student: random.randint(0, 100) for student in names}
# print(new_list)
# even_more_new_list = {student for student in new_list if student[f"{student}"] > 50}
# print(even_more_new_list)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
obj = {word: len(word) for word in sentence.split(' ')}
print(obj)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
print(weather_c.items())

weather_f = {item: (temp_c * 9 / 5) + 32 for (item, temp_c) in weather_c.items()}
print(weather_f)