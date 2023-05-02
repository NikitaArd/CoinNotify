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
    DB_FIELDS = ['id', 'firstname', 'lastname', 'user_id', 'status', 'timediff', 'user_schedule', 'sub_coin_list', '*']

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

    def check_field(self, id_of_user: str, field: str):
        """
        Checks if field is filled
        """
        if field in self.DB_FIELDS:
            self.cur.execute(f"SELECT {field.lower()} FROM subers WHERE user_id = '{id_of_user}';")
        else:
            raise Exception('Invalid field name')

        return bool(self.cur.fetchone()[0])

    def add_user(self, id_of_user: str, firstname: str, lastname: str, timediff: int, status:bool = False):
        """
        Creates new user
        """
        if not self.check_field(id_of_user, '*'):
            self.cur.execute(
                f"INSERT INTO subers(firstname, lastname ,user_id, status, timediff) VALUES('{firstname}', '{lastname}', '{id_of_user}', '{status}', {timediff});")
            self.conn.commit()
            logging('adding', 'New user', id_of_user, firstname, lastname, status)

    def set_user_schedule(self, id_of_user: str, time_list: list):
        """
        Sets user schedule
        """
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

    def set_user_coin_list(self, id_of_user: str, coin_list: list):
        """
        Sets entered by user coin list
        """
        if not self.check_field(id_of_user, '*'):
            return False
        self.cur.execute(f"UPDATE subers SET sub_coin_list = ARRAY{coin_list} WHERE user_id = '{id_of_user}';")
        self.conn.commit()
        return True

    # Updating Subscriber newsletter status OR creating new Subscriber in database
    def newsletter_status(self, id_of_user: str, firstname: str, lastname: str, status: bool):
        """
        Updates users newsletter status
        """
        if self.check_field(id_of_user, '*'):
            # If the users current status is the status he wants to set
            if self.get_user_status(id_of_user) is status:
                return
            self.cur.execute(f"UPDATE subers set status = {status} WHERE user_id = '{id_of_user}';")
            self.conn.commit()
            logging('updating', 'User', id_of_user, firstname, lastname, 'update status on', status)
        else:
            self.add_user(id_of_user, firstname, lastname, status)

    # Returning all Subscribers with given status
    def get_users_with_status(self, status: bool):
        """
        Returns All users with appropriate status
        """
        self.cur.execute(f"SELECT * FROM subers WHERE status='{status}';")
        return list(self.cur.fetchall())

    def get_user(self, id_of_user: str):

        self.cur.execute(f"SELECT * FROM subers WHERE user_id='{id_of_user}';")
        return self.cur.fetchone()

    def get_user_status(self, id_of_user: str):
        """
        Returns status of appropriate user
        """
        self.cur.execute(f"SELECT status FROM subers WHERE user_id='{id_of_user}';")

        return self.cur.fetchone()[0]
