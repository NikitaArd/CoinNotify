# telegram-crypto-bot

Link do bota:

https://t.me/CryptoHandler_bot

</br>

---

</br>

## Spis treści

 - Opis
   - [Opis projektu](#opis)
   - [Komendy](#komendy)
 - Technologię
   - [Biblioteki](#biblioteki)
   - [API](#api)
 - Inna informacja
   - [Plik .env](#env)

</br>

---

## <a id='opis'></a> Opis

Projekt zrobiony we właśnym zakresie w celu zdybcia nowej, i przećwiczenie obecnej wiedzy.

</br>

## <a id='komendy'></a> Bot obsługuje następujące komendy:

| Komenda | Opis |
| ------------- | ------------- |
| /start  | Wywołuje się automatycznie po kliklnięciu przycisku start. Po wpisaniu tej komendy Bot przywita się i **zapyta o czas aby ustawić w jakiej strefie czasowej znajduję się użytkownik**. |
| /crypto  | Bot wysyła listę cenę różnych monet. |
| /add     | Po wpisaniu konmendy Bot zapiszę użytkownika do Newslettera, jeśli użytkownik ma ustawiony **czas** i **listę monet**. |
| /unadd   | Po wpisaniu komendy Bot usunie użytkownika z Newslettera, ale zachowa jego ustawienia **czasu** i **listy monet**. |
| /set_time | Bot prosi o podanie nowego czasu o której ma wysyłać Newsletter. |
| /set_coin_list | Bot prosi o podanie nowej listy monet, które użytkownik chcę dostawać w Newletter. |
| /help | Lista komend i krótki opis projektu oraz jego twórcy. |

</br>

---

</br>

## <a id='biblioteki'></a> Biblioteki

| Nazwa | Wersja |
| ------------- | ------------- |
| PyTelegramBotAPI | 4.10.0 |
| psycopg2 | 2.9.5 |
| APScheduler | 3.10.1 |
| python-dotenv | 1.0.0 |
| cryptocompare | 0.7.6 |

## <a id='api'></a> API


Projekt używa [CryptoCompare API](https://min-api.cryptocompare.com), ze względu na swoją dostępność i brak ograniczeń na zayptania bez klucza.

</br>

---

</br>

## <a id='env'></a> Plik .env

Jeśli chcesz uruchomić ten projekt lokalnie, musiś w folderze projektu umieścić plik **.env**, który będzie zawierał następującą informację.

### Uzupełni
```
# Unikatowy klucz bota
TOKEN=''

# Nazwa bazy danych
PGDATABASE=''

# Nazwa użytkownika
PGUSER=''

# Hasło użytkownika
PGPASSWORD=''

# Adres hosta bazy danych 
PGHOST='127.0.0.1'

# Port hosta bazy danych
PGPORT='5432'
```

### Nie zmieniaj
```
TIME_UNIT='m'
INTERVAL='1'
MAX_USER_TIMES=5
MAX_USER_COINS=5
```