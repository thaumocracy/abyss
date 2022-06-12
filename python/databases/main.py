import pymysql
import json
# не забыть отодрать пароль
con = pymysql.connect('localhost', '',
                      '', 'list_app')

with con:
    cur = con.cursor()

    with open('bbc-books.json',  encoding='utf-8') as json_file:
        data = json.load(json_file)
        sql = 'INSERT INTO books (title,author,image,finished,description) VALUES (%s,%s,%s,%s,%s)'
        for item in data:
            values = (item['title'], item['author'],
                      item['image'], item['finished'], item['description'])
            cur.execute(sql, values)
