import datetime

import telebot
from apscheduler.schedulers.background import BackgroundScheduler

import sys

# Local imports
from assets import *
from tools import (
    DBController,
    get_parse_data,
    logging,
    validate_user_time,
    calc_timezone,
)

bot = telebot.TeleBot(TOKEN)
db = DBController(DB_NAME)


def check_time():
    # If minutes are multiple of 10 ( every 10 minutes do mailing() )
    if not int(datetime.datetime.now().strftime('%M')) % 10:
        mailing(datetime.datetime.now().strftime('%H:%M'))


def mailing(cur_time):
    # Try to Add cur_time into SQL request
    subers = db.get_users_with_status(True)
    table = get_parse_data()

    mailing_count = 0
    for s in subers:
        if cur_time in s[6]:
            mailing_count += 1
            bot.send_message(s[3], table)

    logging('mailing', mailing_count, 'user(s)')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, start_answer)
    bot.send_message(message.chat.id, time_tz_advice)
    bot.register_next_step_handler(message, process_get_time_step)


def process_get_time_step(message):
    # Validate user input time
    if validate_user_time(message.text):
        db.add_user(
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.last_name,
            calc_timezone(message.text)
        )
        bot.send_message(message.chat.id, time_tz_ok)
    else:
        bot.send_message(message.chat.id, invalid_time_tz)
        bot.register_next_step_handler(message, process_get_time_step)


def process_set_schedule_step(message):
    # Getting user input time ['HH:MM', 'HH:MM', 'HH:MM']
    user_time_list = message.text.replace(' ', '').split(',')

    # Validate user input time
    for t in user_time_list:
        if not validate_user_time(t, True):
            bot.send_message(message.chat.id, invalid_time)
            # If isn't valid ask about time again
            bot.register_next_step_handler(message, process_set_schedule_step)
            return

    # Try to write data in to database
    if not db.set_user_schedule(message.from_user.id, user_time_list):
        bot.send_message(message.chat.id, invalid_time)
        bot.register_next_step_handler(message, process_set_schedule_step)

    db.newsletter_status(message.from_user.id, message.from_user.first_name, message.from_user.last_name, True)
    bot.send_message(message.chat.id, set_schedule_success.format('\n'.join(user_time_list)))


@bot.message_handler(commands=['change_time'])
def change_schedule(message):
    bot.send_message(message.chat.id, 'Ustaw nowy czas')
    bot.send_message(message.chat.id, time_format_advice)
    bot.register_next_step_handler(message, process_set_schedule_step)


@bot.message_handler(commands=['add'])
def add(message):
    user_time = db.check_user_set_time(message.from_user.id)
    if not user_time[0]:
        bot.send_message(message.chat.id, "Widzę że nie masz ustawionego czasu")
        bot.send_message(message.chat.id, time_format_advice)
        bot.register_next_step_handler(message, process_set_schedule_step)
    else:
        cur_user_status, cur_user_set_time = db.get_user_status(message.from_user.id)
        # If user already subscribed send an appropriate answer
        if cur_user_status:
            bot.send_message(message.chat.id, already_subscribed.format('\n'.join(cur_user_set_time)))
        else:
            db.newsletter_status(message.from_user.id, message.from_user.first_name, message.from_user.last_name, True)
            bot.send_message(message.chat.id, set_schedule_success.format('\n'.join(user_time[0])))


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
    scheduler.start()
    logging('starting', 'Starting bot work')
    bot.infinity_polling(timeout=10, long_polling_timeout=5)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    if TIME_UNIT == 'h':
        scheduler.add_job(check_time, 'interval', hours=int(INTERVAL))
    elif TIME_UNIT == 'm':
        scheduler.add_job(check_time, 'interval', minutes=int(INTERVAL))
    else:
        logging('error', 'Invalid time unit')
        sys.exit()
    logging('info', 'Logging is turned ON every', INTERVAL, TIME_UNIT)

    main()

    logging('leaving', 'Ending', 'program')
    sys.exit()
