data = None
with open('example.docx', 'r') as file:
    data = file.read()

print(data)

with open('names.txt', 'r') as names:
    for name in names:
        with open(f'./output/letter_to_{name.strip()}.docx', 'w') as letter:
            letter.write(data.replace("[name]", name.strip()))
