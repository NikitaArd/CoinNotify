"""
File with all settings (bot, database, api)
"""

import os
from dotenv import load_dotenv

load_dotenv()

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
