from aiogram import types, Dispatcher

from create_bot import bot, dp
from keyboards.default import menu_kb as nav
from data import config

# admins = config.ADMINS
admins = [123]


# @dp.message_handler(commands=['start'])
async def start_working(message: types.Message):
    if str(message.from_user.id) not in admins:
        await bot.send_message(message.from_user.id,
                               'Здравствуйте, {0.first_name}!\n'
                               'Меня зовут Павел.\n'
                               'Я работаю ветеринарным врачом в г.Иваново более 20-лет.\n'
                               'Надеюсь, я смогу быть Вам полезен\n'
                               'Выберите необходимую команду в меню'.format(message.from_user),
                               reply_markup=nav.mainMenu)
    else:
        await bot.send_message(message.from_user.id, 'Привет, хозяин! Чего изволишь?', reply_markup=nav.adminMenu)


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите услугу для подробной информации:\n '
                                                 '/start - начало работы с ботом\n'
                           # '/lowprice - вывод самых дешёвых отелей в городе\n'
                           # '/highprice — вывод самых дорогих отелей в городе\n'
                           # '/bestdeal — вывод отелей, наиболее подходящих по цене '
                           # 'и расположению от центра\n'
                           # '/history — вывод истории поиска отелей'
                           )


# @dp.message_handler()
async def menu_commands(message: types.Message):
    if message.text == 'Инфо для владельцев животных':
        await bot.send_message(message.from_user.id, 'Инфо для владельцев животных', reply_markup=nav.infoMenu)
    elif message.text == 'Вет услуги':
        await bot.send_message(message.from_user.id, 'Вет услуги', reply_markup=nav.vetServices)
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Вет услуги', reply_markup=nav.mainMenu)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_working, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(menu_commands)
