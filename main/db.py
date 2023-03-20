"""
File with DataBase controller,
to eliminate interfering database queries with business logic
"""

import psycopg2

# Local import
from settings import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    MAX_COUNT_USER_TIME,
    MAX_COUNT_USER_COINS,
)

from tools import logging


class DBController:
    DB_NAME = DB_NAME
    DB_USER = DB_USER
    DB_PASSWORD = DB_PASSWORD
    DB_HOST = DB_HOST
    DB_PORT = DB_PORT
    MAX_COUNT_USER_TIME = MAX_COUNT_USER_TIME
    MAX_COUNT_USER_COINS = MAX_COUNT_USER_COINS

    def __init__(self):
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
            user_schedule text ARRAY[{}],
            sub_coin_list text ARRAY[{}]);""".format(self.MAX_COUNT_USER_TIME,
                                                     self.MAX_COUNT_USER_COINS))
            self.conn.commit()

    # Returning Something if Subscriber exists and Nothing if Subscriber doesn't exist
    def check_user_in_db(self, id_of_user):
        self.cur.execute(f"SELECT * FROM subers WHERE user_id = '{id_of_user}';")
        return self.cur.fetchall()

    def check_user_set_time(self, id_of_user):
        self.cur.execute(f"SELECT user_schedule FROM subers WHERE user_id = '{id_of_user}';")
        return self.cur.fetchone()

    def check_user_set_coin_list(self, id_of_user):
        self.cur.execute(f"SELECT sub_coin_list FROM subers WHERE user_id = '{id_of_user}';")
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

    def set_user_coin_list(self, id_of_user, coin_list):
        if not self.check_user_in_db(id_of_user):
            return False
        self.cur.execute(f"UPDATE subers SET sub_coin_list = ARRAY{coin_list} WHERE user_id = '{id_of_user}';")
        self.conn.commit()
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
        self.cur.execute(f"SELECT status, user_schedule, sub_coin_list FROM subers WHERE user_id='{id_of_user}';")
        data = self.cur.fetchone()
        return data[0], data[1], data[2]