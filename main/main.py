import telebot
from apscheduler.schedulers.background import BackgroundScheduler
import sys

# Local imports
from assets import *
from tools import (
    DBController,
    get_parse_data,
    logging
)

bot = telebot.TeleBot(TOKEN)
db = DBController(DB_NAME)


def mailing():
    subers = db.get_users_with_status(True)
    table = get_parse_data()
    logging('mailing', len(subers), 'subscribers')
    for s in subers:
        bot.send_message(s[3], table)


@bot.message_handler(commands=['start'])
def start(message):
    db.add_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
    bot.send_message(message.chat.id, start_answer)


@bot.message_handler(commands=['add'])
def add(message):
    db.newsletter_status(message.from_user.id, message.from_user.first_name, message.from_user.last_name, True)
    bot.send_message(message.chat.id, newsletter_add)
    

@bot.message_handler(commands=['unadd'])
def unadd(message):
    db.newsletter_status(message.from_user.id, message.from_user.first_name, message.from_user.last_name, False)
    bot.send_message(message.chat.id, newsletter_unadd)


@bot.message_handler(commands=['crypto'])
def crypto(message):
    table = get_parse_data()
    bot.send_message(message.chat.id, table)


@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, help_answer)


def main():
    logging('starting', 'Starting bot work')
    scheduler.start()
    bot.polling(none_stop=True)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    if TIME_UNIT == 'h':
        scheduler.add_job(mailing, 'interval', hours=int(INTERVAL))
    elif TIME_UNIT == 'm':
        scheduler.add_job(mailing, 'interval', minutes=int(INTERVAL))
    else:
        logging('error', 'Invalid time unit')
        sys.exit()
    logging('info', 'Logging is turned ON every', INTERVAL, TIME_UNIT)

    main()

    logging('leaving', 'Ending', 'program')
    sys.exit()
