import requests
from main import write_json
import re

def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]


def get_price(crypto):

    url = 'https://api.coinmarketcap.com/v1/ticker/{}/'.format(crypto)
    r = requests.get(url).json()
    price = r[-1]['price_usd']
    #write_json(r.json(), filename='price.json')
    return round(float(price),2)


def main():
    print(get_price(parse_text('/ripple ss')))

if __name__ == '__main__':
    main()