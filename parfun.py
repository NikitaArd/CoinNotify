import requests
from lxml.html import fromstring
import urllib.response
from prettytable import PrettyTable

aup = '⬆'
adown = '⬇'

def parse():
    response = urllib.request.urlopen('https://www.rbc.ru/crypto/currency/btcusd').read()
    page = fromstring(response)
    cou = page.xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]/text()')
    ra = page.xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]/span/text()')
    tm = page.xpath('/html/body/div[7]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/div[1]/div[2]/span/text()')
    rate = cou[0].replace(' ', '').replace('\n', '')
    chang = ra[0].replace(' ', '').replace('\n', '')
    time = tm[0].replace('\n', '')

    if chang[0] == '+':
        arrow = aup
    elif chang[0] == '-':
        arrow = adown

    answer = f"""
    Bitcoin :
    💲 Kurs : {rate}$

    {arrow} Różnica : {chang}

    📌 Ostatnia aktualizacja : {time}

    """
    return answer