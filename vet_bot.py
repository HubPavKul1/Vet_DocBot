import os
import logging
import logging.config
from threading import Thread
from aiogram.utils import executor
from psycopg2._psycopg import cursor

from create_bot import dp, bot
from flask import Flask, request, Response
import psycopg2 as ps


from handlers import *
from utils.db import create_tables, delete_tables, fill_streets, fill_breeds
from data.config import ADMINS, URL_APP, dict_config
from vet_parser.site_parser import *

# app = Flask(__name__)


logging.config.dictConfig(dict_config)
logger = logging.getLogger('vet_bot')


# def config_logger():
#     logging.config.dictConfig(dict_config)
# @app.route('/', methods=['POST'])
# def index():
#     if request.headers.get('content-type') == 'application/json':
#         pass


async def on_startup(dp):
    await bot.set_webhook(URL_APP)
    await bot.send_message(ADMINS[0], "Я запущен!")
    logger.info('Startup bot')


async def on_shutdown(dp):
    await bot.delete_webhook()
    await bot.close()
    logger.info('Bot shutdown')
    # cursor.close()
    # connection.close()


admin_reg_owner.register_handlers_admin_reg_owner(dp)
admin_reg_address.register_handlers_admin_reg_address(dp)
admin_reg_patient.register_handlers_admin_reg_patient(dp)
admin_reg_order.register_handlers_admin_reg_order(dp)
search_drugs.register_handlers_search_drug(dp)
client.register_handlers_client(dp)
other.register_handlers_other(dp)


if __name__ == '__main__':
    # config_logger()
    # delete_tables()
    # print('tables deleted')
    # create_tables()
    # print('tables created')
    # t1 = Thread(target=fill_streets)
    # t2 = Thread(target=fill_breeds)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # fill_streets()
    # print('all done')
    # fill_breeds()
    # print('breeds added')
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

