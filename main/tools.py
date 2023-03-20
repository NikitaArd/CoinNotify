"""
File with other functions (like formatting and getting API data)
"""

import cryptocompare
import datetime
import re

# Local import
from settings import SERVICED_COINS
from assets import answer


# Returning format answer with Data
def get_crypto_data() -> str:
    cs = cryptocompare.get_price([*SERVICED_COINS], 'USD')
    return answer.format(''.join([f"💲 {SERVICED_COINS[x]}: {cs[x]['USD']}$\n" for x in SERVICED_COINS]))


def get_crypto_data_by_user_settings(subers) -> dict:
    cs = cryptocompare.get_price([*SERVICED_COINS], 'USD')
    coin_prices = {x: f'💲 {SERVICED_COINS[x]} : {cs[x]["USD"]}$' for x in SERVICED_COINS}
    table = dict()

    # Creating a table {'user_id': 'user_naswer'}
    for s in subers:
        table[s[3]] = answer.format('\n'.join([coin_prices[x] for x in s[7]]))

    return table


def format_coin_list(coin_list):
    return [f'{x}: {SERVICED_COINS[x]}' for x in coin_list]


# Printing the specified information
def logging(verb: str, *args):
    print(f'[ {verb.upper()} ] {" ".join([str(x) for x in args])}')


def calc_timezone(user_time: str) -> int:
    return int(user_time.split(':')[0]) - int(datetime.datetime.now().strftime('%H'))


def validate_user_time(input_time: str, validate_minutes=False) -> bool:
    if re.match(r'^([0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', input_time):
        # If validate_minute True, function validate if user enter <minutes> % 10
        return True and (not bool(int(input_time.split(':')[1]) % 10) or not validate_minutes)

    return False


if __name__ == '__main__':
    pass
