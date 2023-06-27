# CoinTrackerBot

🔗 Link to the bot:

https://t.me/CryptoHandler_bot

</br>

---

</br>

## 📌 Content

 - Description
   - [Project description](#description)
   - [Cammands](#commands)
 - Technologies
   - [Libraries](#libs)
   - [API](#api)
 - Other information
   - [.env file](#env)

</br>

---

## <a id='description'></a> 📃 Description

You send to Bot up to 5 timestamps and up to 5 coin abbreviation and It sends You current price of this coins, exactly at your set time !

</br>

## <a id='commands'></a> Bot commands:

| Command | Desription |
| ------------- | ------------- |
| /start  | Calls automaticlly when the start button is clicked. The Bot will say hello and **ask about your current time to set your time zone**. |
| /crypto  | The bot sends you current price of 10 most popular coins. |
| /add     | After entering the command, Bot will add the user to the Newsletter, if user has set **time** and **coin list**. |
| /unadd   | After entering the command Bot will unsubscribe the user from the Newsletter, but save his **time** and **coint list**. |
| /set_time | The Bot will ask to enter new timestamps ( up to 5 ) |
| /set_coin_list | The Bot will ask to enter new 5 coin abbreviation ( up to 5 ) |
| /help | Command list and brief description about this project and author |

</br>

---

</br>

## <a id='libs'></a> Libraries

| Name | Version |
| ------------- | ------------- |
| PyTelegramBotAPI | 4.10.0 |
| psycopg2 | 2.9.5 |
| APScheduler | 3.10.1 |
| python-dotenv | 1.0.0 |
| cryptocompare | 0.7.6 |

## <a id='api'></a> API

The Bot uses [CryptoCompare API](https://min-api.cryptocompare.com), due to its availability and no limit of requests without a key.

</br>

---

</br>

## <a id='env'></a> 🔧 Plik .env

If you want to run this project on your local machine, you need to paste **.env** file in your project directory, which contains next information.

### Complete
```
# Unique bots key
TOKEN=''

# Database name
PGDATABASE=''

# Database User name
PGUSER=''

# Database User password
PGPASSWORD=''

# Host address of database
PGHOST='127.0.0.1'

# Host port of database
PGPORT='5432'
```

### Do not change
```
TIME_UNIT='m'
INTERVAL='1'
MAX_USER_TIMES=5
MAX_USER_COINS=5
```