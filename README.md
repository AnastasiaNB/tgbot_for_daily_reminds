## Бот для напоминаний @Daily_remind_bot
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=plastic&logo=telegram&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=plastic&logo=redis&logoColor=white)
Перед использованием необходимо добавить бота в канал и чат канала,
а также предоставить боту права администратора (отправка сообщений).
#
Перед запуском необходимо создать файл .env с переменными окружения 
(см. .env.example) и изменить переменную ```CHANNEL_NAME``` на имя своего канала.
#
### Запуск: 
```sudo docker-compose up```
#
При необходимости можно изменить текст сообдения, отправляемого ботом (переменная ```text```
в text.py) и время ежедневной отправки сообщения в файле .env в параметрах ```HOUR``` и ```MINUTE```
