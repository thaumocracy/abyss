import json

' TEST THIS IS A TEST'
with open('bbc-books.json',  encoding='utf-8') as json_file:
    data = json.load(json_file)
    for item in data:
        print(item['title'])
