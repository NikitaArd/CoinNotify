import os
from dotenv import load_dotenv

load_dotenv()
"""
File with all assets (ex. messages, tokens ...)
"""

# Settings
TOKEN = os.getenv('TOKEN')
DB_NAME = os.getenv('DATABASE_NAME')
TIME_UNIT = 'h'  # h - hours, m - minutes
INTERVAL = 8  # interval in TIME_UNIT

# Assets
start_answer = """
Witam!
Jestem CryptoBot, pomogę ci sprawdzić kurs Bitcoin-a i Ethereum-a

Jeśli masz pytania nie bój się pisać /help!
"""

help_answer = """
Cześć!
Widzę że potrzebujesz pomocy.
Komendy:
Wpisz /crypto aby sprawdić kurs Bitcoin-a i Ethereum-a
Wpisz /add aby zapisać się do Newsletter
Wpisz /unadd aby wypisać się z Newsletter
Informacja:
Telegram Bot jest napisany w języku programowania Python

Twórca Nikita Smolenskyi
GitHub : https://github.com/NikitaArd?tab=repositories
"""

newsletter_add = "Pomyślnie zapisałeś się do listy mailingowej."
newsletter_unadd = "Pomyślnie wypisałeś się z listy mailingowej."
