import bs4
import asyncio
from pyppeteer import launch

dns_wish_list = [
    ['https://www.dns-shop.ru/product/9947a5e3caab3120/zasitnye-ocki-sp-glasses-comfort-af024/', 999]
]

CLASS = 'product-buy__price'
items = None


async def main():
    global items
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.dns-shop.ru/product/9947a5e3caab3120/zasitnye-ocki-sp-glasses-comfort-af024/')
    items = await page.content()
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

soup = bs4.BeautifulSoup(items, 'html.parser')
price = soup.find(name='div', class_=CLASS)
print(price)

# TODO: Invent some UI and connect this to mobile app. Should also have all the links and graphical hints about sales
