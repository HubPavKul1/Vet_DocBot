from environs import Env
import os

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

TOKEN = env.str("TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
DATABASE_URL = env.str("DATABASE_URL")
# IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
