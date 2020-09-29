import requests
from bs4 import BeautifulSoup
import time

class Currency:
    DOLAR_UAH = 'https://www.google.com/search?q=dollar+to+uah&oq=dollar+&aqs=chrome.1.69i57j0l7.2826j0j7&sourceid=chrome&ie=UTF-8'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(",","."))


    def get_currency_price(self):
        full_page = requests.get(self.DOLAR_UAH, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision":2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",","."))
        if currency >= self.current_converted_price + self.difference:
            print('Currency extremely raised')
        elif currency <= self.current_converted_price + self.difference:
            print('Currency extremely fold')
        print("Now Dollar to UAH: " + str(currency))
        time.sleep(60)
        self.check_currency()

currency = Currency()
currency.check_currency()

