## Бот для напоминаний @Daily_remind_bot
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%2337814A.svg?&style=for-the-badge&logo=celery&logoColor=white)<br/>
Перед использованием необходимо добавить бота в канал и чат канала,
а также предоставить боту права администратора (отправка сообщений).<br/>
####
Перед запуском необходимо создать файл .env с переменными окружения 
(см. .env.example) и изменить переменную ```CHANNEL_NAME``` на имя своего канала.<br/>
####
**Запуск:** ```sudo docker-compose up```<br/>
####
При необходимости можно изменить текст сообщения, отправляемого ботом (переменная ```text```
в text.py) и время ежедневной отправки сообщения в файле .env в переменных ```HOUR``` и ```MINUTE```
