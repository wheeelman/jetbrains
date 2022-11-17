import requests, json


def get_currency_data(user_cur):
    r = requests.get(f'http://www.floatrates.com/daily/{user_cur}.json')
    user_data = json.loads(r.text)
    return user_data

def add_to_cache(cur_data, currency):
    try:
        rates_cache[currency] = cur_data[currency]['rate']
    except KeyError:
        return None

def convert_money(cur_data):
    while True:
        new_cur = input()
        if not new_cur:
            break
        else:
            amount = float(input())

            print('Checking the cache...')
            if new_cur not in rates_cache:
                print('Sorry, but it is not in the cache!')
                add_to_cache(cur_data, new_cur.lower())
            else:
                print('Oh! It is in the cache!')

            print(f"You received {round(rates_cache[new_cur] * amount, 2)} {new_cur.upper()}.")


if __name__ == '__main__':
    rates_cache = {}
    user_currency = input().lower()
    currency_data = get_currency_data(user_currency)
    add_to_cache(currency_data, 'usd')
    add_to_cache(currency_data, 'eur')
    convert_money(currency_data)
