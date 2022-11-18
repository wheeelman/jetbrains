import requests


class CurrencyConverter:
    def __init__(self):
        self.amount = 0.0
        self.from_currency = None
        self.to_currency = None
        self.rates_cache = {}

    def get_request(self, code_currency):
        url = f'http://www.floatrates.com/daily/{code_currency}.json'
        return requests.get(url).json()

    def get_currency(self):
        return input().lower()

    def get_rates_cash(self):
        self.rates_cache['usd'] = self.get_request(code_currency='usd')
        self.rates_cache['eur'] = self.get_request(code_currency='eur')

    def get_rate(self):
        self.rates_cache[self.to_currency] = self.get_request(code_currency=self.to_currency)

    def currency_conversion(self):
        result = round(self.amount * self.rates_cache[self.to_currency][self.from_currency]['inverseRate'], 2)
        return result

    def converter(self):
        self.from_currency = self.get_currency()
        self.get_rates_cash()
        while to_currency := self.get_currency():
            self.to_currency = to_currency
            self.amount = float(input())
            print('Checking the cache...')
            if self.to_currency in self.rates_cache:
                print('Oh! It is in the cache!')
            else:
                print('Sorry, but it is not in the cache!')
                self.get_rate()
            print(f'You received {self.currency_conversion()} {self.to_currency.upper()}.')


def main():
    cc = CurrencyConverter()
    cc.converter()


if __name__ == '__main__':
    main()
