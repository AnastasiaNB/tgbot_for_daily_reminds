## Бот для напоминаний @Daily_remind_bot
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
