codes = {
    "a": "· −",
    "b": "− · · ·",
    "c": "− · − ·",
    "d": "− · ·",
    "e": "·",
    "f": "· · − ·",
    "g": "− − ·",
    "h": "· · · ·",
    "i": "· · ",
    "j": "· − − − ",
    "k": "− · − ",
    "l": "· − · · ",
    "m": "− − ",
    "n": "− · ",
    "o": "− − − ",
    "p": "· − − · ",
    "q": "− − · − ",
    "r": "· − · ",
    "s": "· · · ",
    "t": "− ",
    "u": "· · − ",
    "v": "· · · − ",
    "w": "· − − ",
    "x": "− · · − ",
    "y": "− · − − ",
    "z": "− − · · ",
    "0": "− − − − − ",
    "1": "· − − − − ",
    "2": "· · − − − ",
    "3": "· · · − − ",
    "4": "· · · · − ",
    "5": "· · · · · ",
    "6": "− · · · · ",
    "7": "− − · · · ",
    "8": "− − − · · ",
    "9": "− − − − · ",
    ".": "· − · − · − ",
    ",": "− − · · − − ",
    "?": "· · − − · · ",
    "'": "· − − − − · ",
    "!": "− · − · − − ",
    "/": "− · · − · ",
    "(": "− · − − · ",
    ")": "− · − − · − ",
    "&": "· − · · · ",
    ":": "− − − · · · ",
    ";": "− · − · − · ",
    "=": "− · · · − ",
    "+": "· − · − · ",
    "-": "− · · · · − ",
    "_": "· · − − · − ",
    "$": "· · · − · · − ",
    "@": "· − − · − · ",
    " ": " "
}


def morsefy(string):
    arr = []
    for letter in string.lower():
        arr.append(codes[letter])

    return ' '.join(arr)


print(morsefy('A party of large Orcs, Uruk-hai, sent by Saruman, and other Orcs sent by Sauron and led by Grishnakh, attack the Fellowship. Boromir tries to protect Merry and Pippin from the Orcs, but they kill him and capture the two hobbits. Aragorn, Gimli and Legolas decide to pursue the Orcs taking Merry and Pippin to Saruman. In the kingdom of Rohan, the Orcs are killed by Riders of Rohan, led by Eomer. Merry and Pippin escape into Fangorn Forest, where they are befriended by Treebeard, the oldest of the tree-like Ents. Aragorn, Gimli and Legolas track the hobbits to Fangorn. There they unexpectedly meet Gandalf.'))
