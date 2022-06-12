import requests

NEWS_ENDPOINT = 'https://newsapi.org/v2/everything?q=yndx&apiKey='
STOCK_ENDPOINT = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=YNDX&apikey='

stonks = requests.get(STOCK_ENDPOINT).json()["Time Series (Daily)"]
keys = list(stonks.keys())[:2]
f_percent = (float(stonks[keys[0]]['4. close']) / 100) * 5
yesterday = float(stonks[keys[0]]['4. close'])
pre_yesterday = float(stonks[keys[1]]['4. close'])

diff = abs(yesterday - pre_yesterday)


def print_news(items):
    for item in items:
        print(item['title'])
        print(item['description'])
        print(item['url'])


if diff > f_percent:
    data = requests.get(NEWS_ENDPOINT).json()['articles'][:3]
    print_news(data)  # should be Twilio sms sender, won't bother
