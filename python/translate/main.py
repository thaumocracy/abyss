from translate import Translator

translator = Translator(to_lang="uk")
l = ''

try:
    with open('./povetUkr.txt') as text:
        l = translator.translate(text.read())
except FileNotFoundError:
    print("File not found")

try:
    with open('./second.txt', mode='w', encoding='utf-8') as answer:
        answer.write(l)
except FileNotFoundError:
    print('File does not exist')
