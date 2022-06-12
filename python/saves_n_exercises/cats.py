# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

first_cat = Cat('Bantik', 17)
second_cat = Cat('Second', 5)
third_cat = Cat('Third', 3)

# 2 Create a function that finds the oldest cat


def find_oldest(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


print(
    f"The oldest cat is {find_oldest(first_cat.age, second_cat.age, third_cat.age)} years old.")
