import psycopg2

from pycoingecko import CoinGeckoAPI
import datetime
import re

from assets import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
)


class DBController:
    DB_NAME = DB_NAME
    DB_USER = DB_USER
    DB_PASSWORD = DB_PASSWORD
    DB_HOST = DB_HOST
    DB_PORT = DB_PORT

    def __init__(self, db_name):
        self.DBName = db_name
        with psycopg2.connect(database=self.DB_NAME,
                              user=self.DB_USER,
                              password=self.DB_PASSWORD,
                              host=self.DB_HOST,
                              port=self.DB_PORT) as db:
            self.cur = db.cursor()
            self.conn = db

            self.cur.execute("""CREATE TABLE IF NOT EXISTS subers(
            id SERIAL PRIMARY KEY,
            firstname TEXT,
            lastname TEXT,
            user_id TEXT NOT NULL, 
            status BOOLEAN,
            timezone INT);""")
            self.conn.commit()

    # Returning Something if Subscriber exists and Nothing if Subscriber doesn't exist
    def check_user_in_db(self, id_of_user):
        self.cur.execute(f"SELECT * FROM subers WHERE user_id = '{id_of_user}';")
        return self.cur.fetchall()

    # Creating new Subscriber
    def add_user(self, id_of_user, firstname, lastname, timezone, status=False):
        if not self.check_user_in_db(id_of_user):
            self.cur.execute(
                f"INSERT INTO subers(firstname, lastname ,user_id, status, timezone) VALUES('{firstname}', '{lastname}', '{id_of_user}', '{status}', {timezone});")
            self.conn.commit()
            logging('adding', 'New user', id_of_user, firstname, lastname, status)

    # Updating Subscriber newsletter status OR creating new Subscriber in database
    def newsletter_status(self, id_of_user, firstname, lastname, status):
        if self.check_user_in_db(id_of_user):
            self.cur.execute(f"UPDATE subers set status = {status} WHERE user_id = '{id_of_user}';")
            self.conn.commit()
            logging('updating', 'User', id_of_user, firstname, lastname, status)
        else:
            self.add_user(id_of_user, firstname, lastname, status)

    # Returning all Subscribers with given status
    def get_users_with_status(self, status):
        self.cur.execute(f"SELECT * FROM subers WHERE status='{status}';")
        return list(self.cur.fetchall())


# Returning format answer with Data
def get_parse_data():
    cg = CoinGeckoAPI()
    rate_b = cg.get_price(ids='bitcoin', vs_currencies='usd')
    rate_e = cg.get_price(ids='ethereum', vs_currencies='usd')
    time = datetime.datetime.now().strftime('%H:%M:%S %d-%m')
    # Answer ( what see user )
    answer = f"""
    Bitcoin :
    💲 Kurs Bitcoin-a : {rate_b['bitcoin']['usd']}$
    
    💲 Kurs Ethereum-a : {rate_e['ethereum']['usd']}$
    

    📌 Ostatnia aktualizacja : {time}

    """
    return answer


# Printing the specified information
def logging(verb: str, *args):
    print(f'[ {verb.upper()} ] {" ".join([str(x) for x in args])}')


def calc_timezone(user_time: str) -> int:
    return int(user_time.split(':')[0]) - int(datetime.datetime.utcnow().strftime('%H'))


def validate_user_time(input_time: str) -> bool:
    if re.match(r'^([0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', input_time):
        return True
    return False
