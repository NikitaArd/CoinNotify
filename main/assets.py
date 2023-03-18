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

# Assets
start_answer = """
Witam!
Jestem CryptoBot, pomogę ci sprawdzić kurs Bitcoin i Ethereum

Wpisz /add aby zapisać się do Newsletter.

Jeśli masz pytania nie bój się pisać /help!
"""

set_schedule_success = """
Hura! Czas został ustawiony.
Teraz będę wysyłał do ciebie wiadomości o:
{}
{}
{}

Pomyślnie zostałeś zapizany do Newsletter.
Jeśli chcesz zmienić czas - wpisz /change_time
"""

time_tz_advice = """
Którą godzinę masz teraz ?

To pomoże mi ustawić twóją strefę czasową. :hourglass:
"""

invalid_time_tz = """
Wprowadż godzinę w formacie 24

Przykład:
10:30"""

time_tz_ok = """
Twoje dane zostały zapisane.
Wpisz /help aby dowiedzieć się więcej.
"""

time_format_advice = """
Wpisz po przecinku Godzinę o której chcesz dostawać wiadomości.
Pamiętaj aby godzina była podana w formacie 24 i liczba minut była wielokrotnością 10

Przykład:
10:30, 14:30, 22:40"""

invalid_time = """
Czas został wprowadzony w błędny sposób.
Spróbuj jeszcze raz.

Przykład:
10:30, 14:30, 22:40
"""

help_answer = """
Cześć!
Widzę że potrzebujesz pomocy.
Komendy:
Wpisz /crypto aby sprawdić kurs Bitcoin i Ethereum
Wpisz /add aby zapisać się do Newsletter
Wpisz /unadd aby wypisać się z Newsletter
Informacja:

Twórca Nikita Smolenskyi
GitHub : https://github.com/NikitaArd?tab=repositories
"""

newsletter_add = "Pomyślnie zapisałeś się do listy mailingowej."
newsletter_unadd = "Pomyślnie wypisałeś się z listy mailingowej."
