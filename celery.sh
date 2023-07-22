#!/bin/bash

if [[ "${1}" == "celery" ]]; then
  celery -A tgbot.bot:app worker -l INFO
elif [[ "${1}" == "beat" ]]; then
  celery -A tgbot.bot:app beat
 fi