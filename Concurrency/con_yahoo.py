from threading import Thread
import requests
from lxml import html

class Stock(Thread):
    def __init__(self, symbol):
        super().__init__()

        self.symbol=symbol
        self.url=f'https://finance.yahoo.com/quote/{symbol}'
        self.price=None

    def run(self):
        response=requests.get(self.url)
        if response.status_code==200:
            tree = html.fromstring(response.text)
            price_text = tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()')
            print(price_text)
            if price_text:
                try:
                    self.price = float(price_text[0])
                except ValueError:
                    self.price = None

    def __str__(self) -> str:
        return f'{self.symbol}=={self.price}'

def main():
    symbols = ['MSFT', 'GOOGL', 'AAPL', 'META']
    threads=[Stock(sym) for sym in symbols]

    for t in threads:
        t.start()

    for t in threads:
        t.join()
        print(t)

if __name__=='__main__':
    main()