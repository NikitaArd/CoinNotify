import telebot
from lxml.html import fromstring
import urllib.request
import schedule
from threading import Thread
from parfun import parse
from assets import *
from contrData import DBController

bot = telebot.TeleBot(TOKEN)
db = DBController('users.db')

def mailing():
    subers = db.getUsersWithStatus(True)
    for s in subers:
        table = parse()
        bot.send_message(s[3], table)

@bot.message_handler(commands=['start'])
def start(message):
    db.addUser(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
    bot.send_message(message.chat.id, start_answer)

@bot.message_handler(commands=['add'])
def add(message):
    db.newsLetterStatus(message.from_user.id, True)
    bot.send_message(message.chat.id, newsletter_add)
    

@bot.message_handler(commands=['unadd'])
def unadd(message):
    db.newsLetterStatus(message.from_user.id, False)
    bot.send_message(message.chat.id, newsletter_unadd)

@bot.message_handler(commands=['crypto'])
def crypto(message):
    table =  parse()
    bot.send_message(message.chat.id, table)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_answer)

schedule.every().hour.do(mailing)

def pending():
    while True:
        schedule.run_pending()
    
th = Thread(target=pending)
while True:
    th.start()
    bot.polling(none_stop=True)
