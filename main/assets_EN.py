"""
File with all bots replicas in EN
"""

from settings import (
    MAX_COUNT_USER_TIME,
    MAX_COUNT_USER_COINS,
    SERVICED_COINS,
)

ASSETS_LANG = 'EN'

# Invalid messages
invalid_coin_name = """
Sorry, coin {} is not supported by me or 
it does not exist.
"""

invalid_time = """
The time was entered incorrectly.
Try again.

Examples:
10:30, 14:30, 22:40
lub
9:30, 15:30, 16:30, 18:30
"""

invalid_time_tz = """
Enter the time in 24-h format.

Example:
10:30"""

invalid_max_coin = """
The maximum number of coins that you can set is {}
"""

# Not set data
time_not_set = """
It looks like you have not set up Newsletter schedule.
"""

coin_list_not_set = """
It looks like you have not set up coin list.
"""


# Advices
set_time_coin_advice = """
Type /set_time to change set time,
or /set_coin_list to change coin list.
"""

time_tz_advice = """
What time is it now ?

This will help me set your time zone. 
"""

time_format_advice = """
Enter the time at which you want to get Newsletter after a comma. ( Maximum {} )
Remember that time must be entered in 24-h format and the number of minutes is a multiple of 10

Examples:
10:30, 14:30, 22:40
or
9:30, 15:30, 16:30, 18:30""".format(MAX_COUNT_USER_TIME)

coin_list_advice = """
Enter the coins after a comma. ( Maximum {} )

List of supported coins:

{}
""".format(MAX_COUNT_USER_COINS, '\n'. join(f'{x}: {SERVICED_COINS[x]}' for x in SERVICED_COINS))

set_coins = """
Enter a list of coins that you want to get in Newsletter.
"""

set_new_schedule = 'Set new schedule'

# Information
answer = """
Coin prices:

{}

Last update: Now
"""

set_schedule_success = """
Success! The time has been set.
You schedule looks like this:

{}
"""

user_subscribed = """
You are subscribed to the Newsletter.

Your schedule:
{}

Your coin list:
{}
"""

already_subscribed = """
You are already subscribed to the Newsletter.

Your schedule:
{}

Your coin list:
{}

"""

your_coin_list = """
Your coin list:

{}
"""

time_tz_ok = """
Your data has been saved.
Type /help to learn more.
"""


start_answer = """
What's up!
I'm a CryptoBot, I can help You check cryptocurrency 
or can deliver real-time prices in accordance to Your schedule.

Type /add to subscribe to the Newsletter.

If You want to learn more just type /help.
"""

help_answer = """
Hi!
I see you need help.

Commands:
 - Type /crypto to get prices of 10 most popular coins.
 - Type /add to subscribe to the Newsletter or check set schedule and coin list.
 - Type /set_time to change Newsletter sending schedule.
 - Type /set_coin_list to change Newsletter list of coins.
 - Type /unadd to unsubscribe from the Newsletter.
Information:

Creator: Nikita Smolenskyi
GitHub: https://github.com/NikitaArd?tab=repositories
"""

newsletter_add = "You have successfully subscribed to he Newsletter"
newsletter_unadd = "You have successfully unsubscribed from he Newsletter"
