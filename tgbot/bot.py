import os

from celery import Celery
# from celery.app.base import add_periodic_task
from celery.schedules import crontab
import threading
from dotenv import load_dotenv
from pyrogram import Client

app = Celery('tasks', broker='redis://localhost:6379')

app.conf.timezone = 'Europe/Moscow'

app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'tasks.main',
        # 'schedule': crontab(minute=0, hour=10),
        'schedule': 10.0,
        # 'args': (16, 16)
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


def run_celery():
    argv = [
        "-A", "tasks", 'worker', '--loglevel=info', "--pool=threads"
    ]
    app.worker_main(argv)


# @add_periodic_task(10.0)
@app.task
async def main():
    async with bot_client:
        await bot_client.send_message(channel_name, "hhg hgbkjhg  bghtvfcdsdazsdzds")


if __name__ == '__main__':
    bot_client.start()
    threading.Thread(target=run_celery, daemon=True).start()
    idle()
    bot_client.stop()