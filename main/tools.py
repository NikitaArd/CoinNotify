import psycopg2

import cryptocompare
import datetime
import re

from assets import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    MAX_COUNT_USER_TIME
)


class DBController:
    DB_NAME = DB_NAME
    DB_USER = DB_USER
    DB_PASSWORD = DB_PASSWORD
    DB_HOST = DB_HOST
    DB_PORT = DB_PORT
    MAX_COUNT_USER_TIME = MAX_COUNT_USER_TIME

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
            timediff INT,
            user_schedule text ARRAY[{}]);""".format(self.MAX_COUNT_USER_TIME))
            self.conn.commit()

    # Returning Something if Subscriber exists and Nothing if Subscriber doesn't exist
    def check_user_in_db(self, id_of_user):
        self.cur.execute(f"SELECT * FROM subers WHERE user_id = '{id_of_user}';")
        return self.cur.fetchall()

    def check_user_set_time(self, id_of_user):
        self.cur.execute(f"SELECT user_schedule FROM subers WHERE user_id = '{id_of_user}';")
        return self.cur.fetchone()

    # Creating new Subscriber
    def add_user(self, id_of_user, firstname, lastname, timediff, status=False):
        if not self.check_user_in_db(id_of_user):
            self.cur.execute(
                f"INSERT INTO subers(firstname, lastname ,user_id, status, timediff) VALUES('{firstname}', '{lastname}', '{id_of_user}', '{status}', {timediff});")
            self.conn.commit()
            logging('adding', 'New user', id_of_user, firstname, lastname, status)

    # Set time to send newsletter
    def set_user_schedule(self, id_of_user, time_list: list):
        if 5 < len(time_list) < 1:
            return False

        self.cur.execute(f"SELECT timediff, firstname, lastname FROM subers WHERE user_id = '{id_of_user}';")
        data = self.cur.fetchone()
        user_tz = data[0]
        time_list = [''.join([str(int(x.split(':')[0]) - user_tz), ':', x.split(':')[1]]) for x in time_list]

        self.cur.execute(
            f"UPDATE subers SET user_schedule = ARRAY{time_list} WHERE user_id = '{id_of_user}';")
        self.conn.commit()

        logging('updating', 'User', id_of_user, data[1], data[2], 'set new schedule', *time_list)

        return True

    # Updating Subscriber newsletter status OR creating new Subscriber in database
    def newsletter_status(self, id_of_user, firstname, lastname, status):
        if self.check_user_in_db(id_of_user):
            # If the users current status is the status he wants to set
            if self.get_user_status(id_of_user)[0] is status:
                return
            self.cur.execute(f"UPDATE subers set status = {status} WHERE user_id = '{id_of_user}';")
            self.conn.commit()
            logging('updating', 'User', id_of_user, firstname, lastname, 'update status on', status)
        else:
            self.add_user(id_of_user, firstname, lastname, status)

    # Returning all Subscribers with given status
    def get_users_with_status(self, status):
        self.cur.execute(f"SELECT * FROM subers WHERE status='{status}';")
        return list(self.cur.fetchall())

    def get_user_status(self, id_of_user):
        self.cur.execute(f"SELECT status, user_schedule FROM subers WHERE user_id='{id_of_user}';")
        data = self.cur.fetchone()
        return data[0], data[1]


# Returning format answer with Data
def get_parse_data():
    cs = cryptocompare.get_price(['BTC', 'ETH'], 'USD')
    rate_b = cs['BTC']['USD']
    rate_e = cs['ETH']['USD']
    # Answer ( what see user )
    answer = f"""
    Bitcoin :
    💲 Kurs Bitcoin-a : {rate_b}$
    
    💲 Kurs Ethereum-a : {rate_e}$
    

    📌 Ostatnia aktualizacja : Teraz

    """
    return answer


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
