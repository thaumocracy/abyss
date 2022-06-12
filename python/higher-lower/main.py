from game_data import data
import random
import os
def clear(): return os.system('cls')


art = """
╔═╗┬ ┬┌─┐┌─┐┌─┐  ┌─┐  ┌─┐┌─┐┌─┐
║ ╦│ │├┤ └─┐└─┐  ├─┤  ├─┘│ │├─┘
╚═╝└─┘└─┘└─┘└─┘  ┴ ┴  ┴  └─┘┴ """


def get_person():
    idx = random.randint(0, len(data) - 1)
    return data[idx]


def show_person(person):
    return f'{person["name"]} is a {person["description"]} from {person["country"]} and have {person["follower_count"]} followers'


def compare_persons(chosen, other):
    if chosen["follower_count"] > other["follower_count"]:
        return True
    else:
        return False


def main():
    score = 0
    playing = True
    print(art)
    persons = [get_person(), get_person()]
    while playing:
        if persons[0] == persons[1]:
            persons[0] = get_person()

        print(show_person(persons[0]))
        print(show_person(persons[1]))
        chosen = input("Select A or B \n").lower()
        if chosen == 'a':
            result = compare_persons(persons[0], persons[1])
            if not result:
                print(f"Sorry, that's wrong. Your score is : {score}")
                return
            else:
                persons[1] = get_person()
                score += 1
                print(f"Correct! Score is {score}")
                clear()
                print('---------------------')
                continue
        else:
            result = compare_persons(persons[1], persons[0])

            if not result:
                print(f"Sorry, that's wrong. Your score is : {score}")
                return
            else:
                persons[0] = get_person()
                score += 1
                print(f"Correct! Score is {score}")
                clear()
                print('---------------------')
                continue


main()
