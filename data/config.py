import sys
import os
from environs import Env
from .ascii_filter import *
from .custom_handlers import *


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


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "{levelname} - {asctime} - {module}: {funcName} - {lineno}: {message}",
            "style": '{',
            "datefmt": '%H:%M:%S'
        }
    },
    "handlers": {
        "screen": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": sys.stdout
        },
        "debug_file_handler": {
            "()": CustomFileHandler,
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "debug_logs.txt",
            "mode": "a"
        },
        "error_file_handler": {
            "()": CustomFileHandler,
            "level": "ERROR",
            "formatter": "simple",
            "filename": "errors_logs.txt",
            "mode": "a"
        },
        "info_file_handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "info_logs.txt",
            "when": 'h',
            "interval": 1,
            "backupCount": 10
        }
        # "server_handler": {
        #     "()": ServerHandler,
        #     "level": "DEBUG",
        #     "formatter": "simple"
        # }
    },
    "loggers": {
        "vet_bot": {
            "level": "DEBUG",
            "handlers": ["screen", "debug_file_handler", "error_file_handler"],
            "filters": ['ascii_filter']
        },
        "handlers/client": {
            "level": "DEBUG",
            "handlers": ["screen", "debug_file_handler", "error_file_handler"]
        },
        "handlers/admin_reg_patient": {
            "level": "DEBUG",
            "handlers": ["screen", "debug_file_handler", "error_file_handler"]
        },
    },
    "filters": {
        "ascii_filter": {
            "()": ASCIIFilter
        }
    }
}
