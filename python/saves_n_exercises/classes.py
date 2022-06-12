class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('Im Running')

    def hello(self):
        print(self.name)


player1 = PlayerCharacter('Watson')

print(player1.hello())
