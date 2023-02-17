import os

from aiogram.utils import executor
from psycopg2._psycopg import cursor

from create_bot import dp, bot
from flask import Flask, request, Response
import psycopg2 as ps


from handlers import *
from utils.db import create_tables
from data.config import ADMINS, URL_APP

app = Flask(__name__)


# @app.route('/', methods=['POST'])
# def index():
#     if request.headers.get('content-type') == 'application/json':
#         pass


async def on_startup(dp):
    await bot.set_webhook(URL_APP)
    await bot.send_message(ADMINS[0], "Я запущен!")


async def on_shutdown(dp):
    await bot.delete_webhook()
    await bot.close()
    # cursor.close()
    # connection.close()


admin_reg_owner.register_handlers_admin_reg_owner(dp)
admin_reg_address.register_handlers_admin_reg_address(dp)
admin_reg_patient.register_handlers_admin_reg_patient(dp)
admin_reg_order.register_handlers_admin_reg_order(dp)
client.register_handlers_client(dp)
other.register_handlers_other(dp)


if __name__ == '__main__':
    create_tables()
    executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown, on_startup=on_startup)
    # executor.start_webhook(
    #     dispatcher=dp,
    #     webhook_path='',
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host="0.0.0.0",
    #     port=int(os.environ.get("PORT", 5000))
    # )

