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
DB_PORT = os.getenv('PGPORT ')

# Assets
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
Wpisz /crypto aby sprawdić kurs Bitcoin i Ethereum
Wpisz /add aby zapisać się do Newsletter
Wpisz /unadd aby wypisać się z Newsletter
Informacja:

Twórca Nikita Smolenskyi
GitHub : https://github.com/NikitaArd?tab=repositories
"""

newsletter_add = "Pomyślnie zapisałeś się do listy mailingowej."
newsletter_unadd = "Pomyślnie wypisałeś się z listy mailingowej."
