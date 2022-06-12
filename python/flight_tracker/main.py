import requests
import datetime as dt
import calendar

sheets_url = 'https://api.sheety.co/'

sheets_data = requests.get(url=sheets_url).json()['prices']


# print()

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return dt.date(year, month, day)


def calc_median(items):
    num = 0
    for item in items:
        num += item['price']
    return num / len(items)


def get_best_offer(median, data):
    minimum = data[0]
    for item in data:
        if minimum['price'] > item['price']:
            minimum = item
    return median, minimum['price'], minimum['deep_link'], data[0]['countryTo']['name']


now = dt.datetime.now()
next_month = add_months(now, 1)


def get_by_iata(iata):
    url = 'https://tequila-api.kiwi.com/v2/search'
    api = ''

    headers = {
        "apikey": api,
    }
    url_config = {
        "curr": "RUB",
        "fly_from": "MOW",
        "fly_to": f"{iata}",
        "date_from": now.strftime("%d/%m/%Y"),
        'date_to': next_month.strftime("%d/%m/%Y"),
        "limit": 100
    }
    resp = requests.get(url=url, headers=headers, params=url_config).json()
    data = resp['data']
    median = calc_median(data)
    return get_best_offer(median, data)


def get_offers(items):
    arr = []
    for item in items:
        arr.append(get_by_iata(item['iataCode']))
    return arr


print(get_offers(sheets_data))
