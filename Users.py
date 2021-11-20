import sqlite3
import telebot
from lxml.html import fromstring
import urllib.request
import schedule
from threading import Thread
from parfun import parse

conn = sqlite3.connect(r'users.db', check_same_thread=False)
cur = conn.cursor()

bot = telebot.TeleBot("")

def mailing():
    subers = list(cur.execute("SELECT * FROM `subers` WHERE status=1").fetchall())
    for s in subers:
        table = parse()
        bot.send_message(s[3], table)

cur.execute("""CREATE TABLE IF NOT EXISTS subers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT,
    lastname TEXT,
    user_id TEXT, 
    status INT);""")
conn.commit()

def adder(id_of_user, firstname, lastname):
    user_id = id_of_user
    status = 1
    cur.execute(f"INSERT INTO subers(firstname, lastname ,user_id, status) VALUES('{firstname}', '{lastname}', '{user_id}', '{status}');")
    conn.commit()

def updater(id_of_user):
    user_id = id_of_user
    status = 1
    cur.execute(f"UPDATE subers set status = {status} WHERE user_id = {user_id}")
    conn.commit()

@bot.message_handler(commands=['start'])
def start(message):
    start_answer = """
    Witam!
    Jestem CryptoBot, pomogę ci sprawdzić kurs Bitcoin
    
    Jeśli masz pytania nie bój się pisać /help!
    """
    bot.send_message(message.chat.id, start_answer)

@bot.message_handler(commands=['add'])
def add(message):
    result = str(cur.execute(f"SELECT * FROM subers WHERE user_id = {message.from_user.id}").fetchall())
    result = result.replace('[]','')
    if result == '':
        adder(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
    else:
        updater(message.from_user.id)
    bot.send_message(message.chat.id, "Pomyślnie zapisałeś się do newslettera.")
    

@bot.message_handler(commands=['unadd'])
def unadd(message):
    user_id = message.from_user.id
    status = 0
    cur.execute(f"UPDATE subers set status = {status} WHERE user_id = {user_id}")
    conn.commit()
    bot.send_message(message.chat.id, "Pomyślnie wypisałeś się z listy mailingowej.")

@bot.message_handler(commands=['crypto'])
def crypto(message):
    table =  parse()
    bot.send_message(message.chat.id, table)

@bot.message_handler(commands=['help'])
def help(message):
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
    bot.send_message(message.chat.id, help_answer)

schedule.every().hour.do(mailing)

def pending():
    while True:
        schedule.run_pending()
    
th = Thread(target=pending)
while True:
    th.start()
    bot.polling(none_stop=True)
