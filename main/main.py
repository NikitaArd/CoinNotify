import datetime

import telebot
from apscheduler.schedulers.background import BackgroundScheduler

import sys

# Local imports
from settings import (
    TOKEN,
    SERVICED_COINS,
    MAX_COUNT_USER_COINS,
    TIME_UNIT,
    INTERVAL
)
from assets import *
from db import DBController
from tools import (
    logging,
    validate_user_time,
    calc_timezone,
    format_coin_list,
    get_crypto_data,
    get_crypto_data_by_user_settings
)

bot = telebot.TeleBot(TOKEN)
db = DBController()


def check_time():
    # If minutes are multiple of 10 ( every 10 minutes do mailing() )
    if not int(datetime.datetime.now().strftime('%M')) % 10:
        mailing(datetime.datetime.now().strftime('%H:%M'))


def mailing(cur_time):
    # Try to Add cur_time into SQL request
    subers = db.get_users_with_status(True)
    table = get_crypto_data_by_user_settings(subers)

    # Step 1 generating Dict {user_id: custom_user_answer}
    # Step 2 sending all messages

    mailing_count = 0
    for s in subers:
        if cur_time in s[6]:
            mailing_count += 1
            bot.send_message(s[3], table[s[3]])

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


def process_set_schedule_step(message, single_mode=True):
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

    # db.newsletter_status(message.from_user.id, message.from_user.first_name, message.from_user.last_name, True)
    bot.send_message(message.chat.id, set_schedule_success.format('\n'.join(user_time_list)))

    if not single_mode:
        add(message)


@bot.message_handler(commands=['set_coin_list'])
def set_coin_list(message):
    bot.send_message(message.chat.id, set_coins)
    bot.send_message(message.chat.id, coin_list_advice)
    bot.register_next_step_handler(message, process_set_coin_list_step)


def process_set_coin_list_step(message, single_mode=True):
    coin_list = message.text.replace(' ', '').upper().split(',')

    if len(coin_list) > MAX_COUNT_USER_COINS:
        bot.send_message(message.chat.id, invalid_max_coin.format(MAX_COUNT_USER_COINS))
        bot.register_next_step_handler(message, process_set_coin_list_step)
        return

    # Check if user input coins are serviced by the server
    for coin in coin_list:
        if coin not in SERVICED_COINS:
            bot.send_message(message.chat.id, invalid_coin_name.format(coin))
            bot.register_next_step_handler(message, process_set_coin_list_step)
            return

    if not db.set_user_coin_list(message.from_user.id, coin_list):
        bot.send_message(message.chat.id, invalid_coin_name)
        bot.register_next_step_handler(message, process_set_coin_list_step)

    bot.send_message(message.chat.id, your_coin_list.format('\n'.join(format_coin_list(coin_list))))

    if not single_mode:
        add(message)


@bot.message_handler(commands=['set_time'])
def change_schedule(message):
    bot.send_message(message.chat.id, 'Ustaw nowy czas')
    bot.send_message(message.chat.id, time_format_advice)
    bot.register_next_step_handler(message, process_set_schedule_step)


@bot.message_handler(commands=['add'])
def add(message):
    user_time = db.check_user_set_time(message.from_user.id)
    user_coin_list = db.check_user_set_coin_list(message.from_user.id)
    if not user_time[0]:
        bot.send_message(message.chat.id, time_not_set)
        bot.send_message(message.chat.id, time_format_advice)
        bot.register_next_step_handler(message, process_set_schedule_step, single_mode=False)

    elif not user_coin_list[0]:
        bot.send_message(message.chat.id, coin_list_not_set)
        bot.send_message(message.chat.id, coin_list_advice)
        bot.register_next_step_handler(message, process_set_coin_list_step, single_mode=False)

    else:
        cur_user_status, cur_user_set_time, cur_user_coin_list = db.get_user_status(message.from_user.id)
        # If user already subscribed send an appropriate answer
        if cur_user_status:
            bot.send_message(message.chat.id, already_subscribed.format('\n'.join(cur_user_set_time),
                                                                        '\n'.join(
                                                                            format_coin_list(cur_user_coin_list))))
            bot.send_message(message.chat.id, set_time_coin_advice)
        else:
            db.newsletter_status(message.from_user.id, message.from_user.first_name, message.from_user.last_name, True)
            bot.send_message(message.chat.id, user_subscribed.format('\n'.join(user_time[0]),
                                                                     '\n'.join(format_coin_list(cur_user_coin_list))))
            bot.send_message(message.chat.id, set_time_coin_advice)


@bot.message_handler(commands=['unadd'])
def unadd(message):
    db.newsletter_status(message.from_user.id, message.from_user.first_name, message.from_user.last_name, False)
    bot.send_message(message.chat.id, newsletter_unadd)


@bot.message_handler(commands=['crypto'])
def crypto(message):
    table = get_crypto_data()
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
