from aiogram.utils import executor
from create_bot import dp, bot
import psycopg2 as ps
from flask import Flask, request

from handlers import *
from data.config import ADMINS

app = Flask(__name__)


async def on_shutdown(dp):
    await bot.close()
    # cursor.close()
    # conn.close()


async def on_startup(dp):
    await bot.send_message(ADMINS[0], "Я запущен!")

admin_reg_owner.register_handlers_admin_reg_owner(dp)
admin_reg_address.register_handlers_admin_reg_address(dp)
admin_reg_patient.register_handlers_admin_reg_patient(dp)
admin_reg_order.register_handlers_admin_reg_order(dp)
client.register_handlers_client(dp)
other.register_handlers_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown, on_startup=on_startup)

