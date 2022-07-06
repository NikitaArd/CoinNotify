import sqlite3


class DBController():
	DBname = ''
	conn = None
	cur = None
	def __init__(self, db_name):
		self.DBName = db_name
		self.conn = sqlite3.connect(db_name, check_same_thread=False)
		self.cur = self.conn.cursor()

		self.cur.execute("""CREATE TABLE IF NOT EXISTS subers(
		    id INTEGER PRIMARY KEY AUTOINCREMENT,
		    firstname TEXT,
		    lastname TEXT,
		    user_id TEXT, 
		    status BOOLEAN);""")
		self.conn.commit()

	def addUser(self, id_of_user, firstname, lastname):
	    status = False
	    self.cur.execute(f"INSERT INTO subers(firstname, lastname ,user_id, status) VALUES('{firstname}', '{lastname}', '{id_of_user}', '{status}');")
	    self.conn.commit()

	def newsLetterStatus(self, id_of_user, status):
		self.cur.execute(f"UPDATE subers set status = {status} WHERE user_id = {id_of_user}")
		self.conn.commit()

	def getUsersWithStatus(self, status):
		response = self.cur.execute(f"SELECT * FROM `subers` WHERE status={status}").fetchall()
		return list(response)
