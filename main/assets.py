import os
from dotenv import load_dotenv

load_dotenv()
"""
File with all assets (ex. messages, tokens ...)
"""

# Bot Settings
TOKEN = os.getenv('TOKEN')

# Scheduler settings
TIME_UNIT = os.getenv('TIME_UNIT')  # h - hours, m - minutes
INTERVAL = os.getenv('INTERVAL')  # interval in TIME_UNIT

# DataBase Settings
DB_NAME = os.getenv('PGDATABASE')
DB_USER = os.getenv('PGUSER')
DB_PASSWORD = os.getenv('PGPASSWORD')
DB_HOST = os.getenv('PGHOST')
DB_PORT = os.getenv('PGPORT')

MAX_COUNT_USER_TIME = int(os.getenv('MAX_USER_TIMES'))
MAX_COUNT_USER_COINS = int(os.getenv('MAX_USER_COINS'))

SERVICED_COINS = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
    'USDT': 'Tether',
    'BNB': 'BNB',
    'USDC': 'USD Coin',
    'XRP': 'XRP',
    'ADA': 'Cardano',
    'MATIC': 'Polygon',
    'DOGE': 'Dogecoin',
    'BUSD': 'Binance USD',
}

# Assets
answer = """
Cena monet:

{}

Ostatnia aktualizacja: Teraz
"""

start_answer = """
Witam!
Jestem CryptoBot, pomogę ci sprawdzić kurs Bitcoin i Ethereum

Wpisz /add aby zapisać się do Newsletter.

Jeśli masz pytania nie bój się pisać /help!
"""

set_schedule_success = """
Hura! Czas został ustawiony.
Twój harmonogram wygląda tak:

{}
"""

already_subscribed = """
Już jesteś zapiany do Newslettera.

Twój ustawiony czas:
{}

Twoje ustawione monety:
{}

"""

user_subscribed = """
Jesteś zapisany do Newsletter.

Twój ustawiony czas:
{}

Twoje ustawione monety:
{}
"""

set_time_coin_advice = """
Wpsiz /set_time aby zmienić ustawiony czas.
Lub /set_coin_list aby zmienić ustawiony czas.
"""

time_not_set = """
Widzę że nie masz ustawionego czasu wysyłania Newsletter.
"""

coin_list_not_set = """
Widzę że nie masz ustawionej listy monet.
"""

your_coin_list = """
Twoja lista monet:

{}
"""

time_tz_advice = """
Którą godzinę masz teraz ?

To pomoże mi ustawić twóją strefę czasową. :hourglass:
"""

set_coins = """
Wpisz listę monet które chcesz otrzymywać w Newsletter.
"""

invalid_time_tz = """
Wprowadż godzinę w formacie 24

Przykład:
10:30"""

invalid_coin = """
Przepraszam, moneta {} nie jest obługiwana przeze mnie,
lub ona nie instnieje.
"""

invalid_max_coin = """
Maksymalna liczba ostawionych monet to {}
"""

invalid_coin_1 = """
Niestetu nie mogę znajść ciebie na swojej liscie.
Wpisz /start.
"""

time_tz_ok = """
Twoje dane zostały zapisane.
Wpisz /help aby dowiedzieć się więcej.
"""

time_format_advice = """
Wpisz po przecinku Godzinę o której chcesz dostawać wiadomości. ( Maskymalnie 5 )
Pamiętaj aby godzina była podana w formacie 24 i liczba minut była wielokrotnością 10

Przykład:
10:30, 14:30, 22:40
 lub
9:30, 15:30, 16:30, 18:30"""

coin_list_advice = """
Wpisz po przecinku sombol monety. (Maksymalnie {})

Lista obsługiwanych monet:

{}
""".format(MAX_COUNT_USER_COINS, '\n'. join(f'{x}: {SERVICED_COINS[x]}' for x in SERVICED_COINS))

invalid_time = """
Czas został wprowadzony w błędny sposób.
Spróbuj jeszcze raz.

Przykład:
10:30, 14:30, 22:40
 lub
9:30, 15:30, 16:30, 18:30
"""

help_answer = """
Cześć!
Widzę że potrzebujesz pomocy.
Komendy:
Wpisz /crypto aby sprawdić kurs Bitcoin i Ethereum
Wpisz /add aby zapisać się do Newsletter lub sprawdzić bierzący rozkład wysyłania Newsletter
Wpisz /change_time aby zmienić ustawiony rozkład
Wpisz /unadd aby wypisać się z Newsletter
Informacja:

Twórca Nikita Smolenskyi
GitHub : https://github.com/NikitaArd?tab=repositories
"""

newsletter_add = "Pomyślnie zapisałeś się do listy mailingowej."
newsletter_unadd = "Pomyślnie wypisałeś się z listy mailingowej."
