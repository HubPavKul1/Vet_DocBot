from environs import Env
import os

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

TOKEN = env.str("TOKEN")  # Забираем значение типа str
URL_APP = env.str("URL_APP")
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов

PHONE = env.str("PHONE")
EMAIL = env.str("EMAIL")
TELEGRAM = env.str("TELEGRAM")
VIBER = env.str("VIBER")

PG_HOST = env.str("PG_HOST")  # Тоже str, но для айпи адреса хоста
USER = env.str("USER")
PASSWORD = env.str("PASSWORD")
DBNAME = env.str("DBNAME")

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{PG_HOST}:5432/{DBNAME}"
