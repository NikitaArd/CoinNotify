import sqlite3

from pycoingecko import CoinGeckoAPI
import datetime


class DBController:
    # Connecting or Creating DataBase
    def __init__(self, db_name):
        self.DBName = db_name
        with sqlite3.connect(db_name, check_same_thread=False) as db:
            self.cur = db.cursor()
            self.conn = db

            self.cur.execute("""CREATE TABLE IF NOT EXISTS subers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            user_id TEXT, 
            status BOOLEAN);""")

    # Returning Something if Subscriber exists and Nothing if Subscriber doesn't exist
    def check_user_in_db(self, id_of_user):
        return self.cur.execute(f"SELECT * FROM subers WHERE user_id = {id_of_user}").fetchall()

    # Creating new Subscriber
    def add_user(self, id_of_user, firstname, lastname, status=False):
        self.cur.execute(
            f"INSERT INTO subers(firstname, lastname ,user_id, status) VALUES('{firstname}', '{lastname}', '{id_of_user}', '{status}');")
        self.conn.commit()
        logging('adding', 'New user', id_of_user, firstname, lastname, status)

    # Updating Subscriber newsletter status OR creating new Subscriber in database
    def newsletter_status(self, id_of_user, firstname, lastname, status):
        if self.check_user_in_db(id_of_user):
            self.cur.execute(f"UPDATE subers set status = {status} WHERE user_id = {id_of_user}")
            self.conn.commit()
            logging('updating', 'User', id_of_user, firstname, lastname, status)
        else:
            self.add_user(id_of_user, firstname, lastname, status)

    # Returning all Subscribers with given status
    def get_users_with_status(self, status):
        response = self.cur.execute(f"SELECT * FROM `subers` WHERE status={status}").fetchall()
        return list(response)


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
