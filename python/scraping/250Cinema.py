import requests
from bs4 import BeautifulSoup
import json

response = requests.get(
    'https://ru.wikipedia.org/wiki/250_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%BE%D0%B2_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_IMDb')


soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('tbody')
table_rows = table.find_all('tr')


def get_data(rows):
    items = []
    for row in rows:
        data = row.select('td')
        temp = []
        for item in data:
            temp.append(item.getText())
        items.append(temp)
    return items


def sort_data(data):
    mov_list = []
    print('this is a data')
    for item in data[1:]:
        mov_list.append({
            'index': item[0],
            'title': item[1],
            'year': item[2],
            'director': item[3],
            'genres': item[4]
        })
    print('this is a data')
    return mov_list


data = sort_data(get_data(table_rows))
output = json.dumps(data, ensure_ascii=False).encode('utf8')

with open('movies.json', mode="wb") as file:
    file.write(output)
    print('All is well?')
