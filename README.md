# Игровой Discord бот - Симулятор майнера

## Рабочие команды
1. Профиль
    - Просмотр своего профиля
    - ~~Редактирование описание профиля~~
    - ~~Просмотр профиля другого пользователя~~
    - ~~Просмотр купленных майнеров у себя/другого пользователя~~
    - ~~Перевод денег другому пользователю~~
2. Магазин
    - Просмотр обычных/~~PREMIUM~~ майнеров
    - Добавление в магазин обычных/~~PREMIUM~~ майнеров
    - ~~Редактирование обычных/PREMIUM майнеров~~

## Установка бота
1. [Установить Python](https://www.python.org/downloads/)
2. Установить библиотеку **discord** ```pip install discord```
3. Клонирование репозитория ```git clone https://github.com/mohovoy/mining-game-bot.git```
4. Создание бота (*если есть, можно пропустить*):
    - Переходим в раздел **[Applications](https://discord.com/developers/applications)**, жмём кнопку **New application**
    - Даём имя боту, соглашаемся с правилами Discord'а, тыкаем на **Create**
    - Раздел **Bot** -> жмем **Add bot** -> соглашаемся
    - Бот создан!
    - P.S Можно также поставить аватарку для нашего бота
5. Создание токена
    - Для правильной работы бота, поставить галочки в разделах **PRESENCE INTENT**, **SERVER MEMBERS INTENT**, **MESSAGE CONTENT INTENT**
    - В этом разделе жмем кнопку **Reset token**, соглашаемся
    - В папке репозитория создать файл **token.txt**, вписать туда вписать полученный токен
6. Запуск
    - Открываем консоль, пишем `python main.py`
    - Если сделали все правильно, бот должен выдать сообщение **[*Имя вашего бота*] запущен и готов к работе!**

<details>
    <summary>Заготовка для магазина</summary>

```sql
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer KA3', '100', '5', '1');
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer K7', '300', '9', '1');
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer L7', '500', '13', '2');
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer A5', '700', '19', '2');
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer A1', '900', '27', '3');
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer I7', '1100', '35', '3');
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer E4', '1300', '43', '4');
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer C4', '1500', '59', '4');
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer 01', '1700', '71', '5');
INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('Hashminer A2', '1900', '87', '5');
```
</details>

Для самостоятельной добавления манера в магазин, в чате Discord нужно писать команду **$add i1 i2 i3 i4**, где:
* **i1** - Стоимость майнера
* **i2** - Мощность майнера
* **i3** - Уровень для покупки
* **i4** - Название майнера