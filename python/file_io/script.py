# my_file = open('test.txt')

# # print(my_file.read())

# print(my_file.readline(5))

# my_file.close()

with open('test.txt', mode="r+") as text:
    print(text.readlines())
    print(text.write('BUTTHOLE'))
