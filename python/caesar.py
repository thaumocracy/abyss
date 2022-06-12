alphabet = list('abcdefghijklmnopqrstuvwxyz')


def encode_letter(letter, tick):
    letter_index = alphabet.index(letter)
    if letter_index + tick >= len(alphabet) - 1:
        letter_index = abs(len(alphabet) - (letter_index + tick))
    else:
        letter_index += tick
    return alphabet[letter_index]


def encode(word, tick):
    """
    Working as decode with negative tick
    """
    answer = ''
    for letter in word:
        answer += encode_letter(letter, tick)
    return answer

# doesnt work with really big tick numbers


print(encode('zaibatsu', 3))
print(encode('cdledwvx', -3))
