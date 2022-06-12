class User():
    def sign_in(self):
        print("User logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with {self.power}")


class Archer(User):
    def __init__(self, name, number_of_arrows):
        self.name = name
        self.number_of_arrows = number_of_arrows

    def attack(self):
        self.number_of_arrows -= 1
        print(f"Attacking with arrows! {self.number_of_arrows} left!")


wizard1 = Wizard('Merlin', "Fukking super-magic power")
archer1 = Archer('Robin', 100)

print(archer1.sign_in())
print(archer1.attack())
print(wizard1.attack())
