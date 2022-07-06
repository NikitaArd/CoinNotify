import requests
from lxml.html import fromstring
import urllib.response
from pycoingecko import CoinGeckoAPI
import datetime

def parse():
    cg = CoinGeckoAPI()
    rate = cg.get_price(ids='bitcoin', vs_currencies='usd')
    time = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    answer = f"""
    Bitcoin :
    💲 Kurs : {rate['bitcoin']['usd']}$

    📌 Ostatnia aktualizacja : {time}

    """
    return answer

if __name__ == '__main__':
    print(parse())