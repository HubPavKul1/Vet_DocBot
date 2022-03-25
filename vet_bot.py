from aiogram.utils import executor
from create_bot import dp

# @dp.message_handler()
# async def greeting(message: types.Message):
#     if message.text.lower() == 'привет':
#         await bot.send_message(message.text, 'Привет, я ветеринарный бот. Нажми /start для начала работы. '
#                                              'Чтобы узнать, как мной управлять, набери /help')
#
#     else:
#         await bot.send_message(message.text, 'Не понял команду, нажми /help для выбора доступных команд')
from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True)
