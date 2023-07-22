import os
from datetime import date

import emoji
from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv
from pyrogram import Client

from tgbot.text import text

app = Celery('tasks', broker='redis://localhost:6379')

app.conf.timezone = 'Europe/Moscow'

app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'send_message',
        'schedule': crontab(minute=0, hour=8),
    },
}

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
channel_name = os.getenv('CHANNEL_NAME')

bot_client = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


@app.task(name='send_message')
def send_message():
    dt = date.today()
    with bot_client:
        bot_client.send_message(
            channel_name,
            emoji.emojize(
                f"{text}{dt}"
            )
        )
