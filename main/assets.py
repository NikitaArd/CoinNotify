import os
from dotenv import load_dotenv

load_dotenv()
"""
File with all assets (ex. messages, tokens ...)
"""

# Settings
TOKEN = os.getenv('TOKEN')
DB_NAME = os.getenv('DATABASE_NAME')
TIME_UNIT = 'm'  # h - hours, m - minutes
INTERVAL = 1  # interval in TIME_UNIT

# Assets
start_answer = """
Witam!
Jestem CryptoBot, pomogę ci sprawdzić kurs Bitcoin

Jeśli masz pytania nie bój się pisać /help!
"""

help_answer = """
Cześć!
Widzę że potrzebujesz pomocy.
Komendy:
Wpisz /crypto aby sprawdić kurs Bitcoina
Wpisz /add aby zapisać się do Newsletter
Wpisz /unadd aby wypisać się z Newsletter
Informacja:
Telegram Bot jest napisany na jęsyku programowania Python

Twórca Nikita Smolenskyi
GitHub : https://github.com/NikitaArd?tab=repositories
"""

newsletter_add = "Pomyślnie zapisałeś się do newslettera."
newsletter_unadd = "Pomyślnie wypisałeś się z listy mailingowej."
