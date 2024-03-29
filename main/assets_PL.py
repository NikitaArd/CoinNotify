"""
File with all bots replicas in PL
"""

from settings import (
    MAX_COUNT_USER_TIME,
    MAX_COUNT_USER_COINS,
    SERVICED_COINS,
)

ASSETS_LANG = 'PL'

# Invalid messages
invalid_coin_name = """
Przepraszam, moneta {} nie jest obsługiwana przeze mnie,
lub ona nie instnieje.
"""

invalid_time = """
Czas został wprowadzony w błędny sposób.
Spróbuj jeszcze raz.

Przykład:
10:30, 14:30, 22:40
lub
9:30, 15:30, 16:30, 18:30
"""

invalid_time_tz = """
Wprowadż godzinę w formacie 24

Przykład:
10:30"""

invalid_max_coin = """
Maksymalna liczba monet, które możesz ustawić to {}
"""

# Not set data
time_not_set = """
Widzę że nie masz ustawionego czasu wysyłania Newsletter.
"""

coin_list_not_set = """
Widzę że nie masz ustawionej listy monet.
"""


# Advices
set_time_coin_advice = """
Wpisz /set_time aby zmienić ustawiony czas,
Lub /set_coin_list aby zmienić ustawioną listę monet.
"""

time_tz_advice = """
Którą godzinę masz teraz ?

To pomoże mi ustawić twoją strefę czasową. 
"""

time_format_advice = """
Wpisz po przecinku Godzinę o której chcesz dostawać wiadomości. ( Maskymalnie {} )
Pamiętaj aby godzina była podana w formacie 24 i liczba minut była wielokrotnością 10

Przykład:
10:30, 14:30, 22:40
 lub
9:30, 15:30, 16:30, 18:30""".format(MAX_COUNT_USER_TIME)

coin_list_advice = """
Wpisz po przecinku sombol monety. (Maksymalnie {})

Lista obsługiwanych monet:

{}
""".format(MAX_COUNT_USER_COINS, '\n'. join(f'{x}: {SERVICED_COINS[x]}' for x in SERVICED_COINS))

set_coins = """
Wpisz listę monet które chcesz otrzymywać w Newsletter.
"""

# Information
answer = """
Cena monet:

{}

Ostatnia aktualizacja: Teraz
"""

set_schedule_success = """
Hura! Czas został ustawiony.
Twój harmonogram wygląda tak:

{}
"""

user_subscribed = """
Jesteś zapisany do Newsletter.

Twój ustawiony czas:
{}

Twoje ustawione monety:
{}
"""

already_subscribed = """
Już jesteś zapisany do Newslettera.

Twój ustawiony czas:
{}

Twoje ustawione monety:
{}

"""

your_coin_list = """
Twoja lista monet:

{}
"""

time_tz_ok = """
Twoje dane zostały zapisane.
Wpisz /help aby dowiedzieć się więcej.
"""


start_answer = """
Witam!
Jestem CryptoBot, pomogę ci sprawdzić kurs Bitcoin i Ethereum

Wpisz /add aby zapisać się do Newsletter.

Jeśli masz pytania nie bój się pisać /help!
"""

help_answer = """
Cześć!
Widzę że potrzebujesz pomocy.

Komendy:
 - Wpisz /crypto aby sprawdić cenę 10 najpopularniejszych monet.
 - Wpisz /add aby zapisać się do Newsletter lub sprawdzić aktualny czas wysyłania Newsletter.
 - Wpisz /set_time aby zmienić ustawiony czas wysyłania Newsletter.
 - Wpisz /set_coin_list aby zmienić ustawioną listę monet w Newsletter.
 - Wpisz /unadd aby wypisać się z Newsletter.
Informacja:

Twórca Nikita Smolenskyi
GitHub: https://github.com/NikitaArd?tab=repositories
"""

newsletter_add = "Pomyślnie zapisałeś się do listy mailingowej."
newsletter_unadd = "Pomyślnie wypisałeś się z listy mailingowej."
