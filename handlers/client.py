from aiogram import types, Dispatcher

from create_bot import bot, dp
from keyboards.default import menu_kb as nav
from data import config

admins = config.ADMINS
# admins = [123]


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
        await bot.send_message(message.from_user.id, 'Привет, хозяин! Чего изволишь?',
                               reply_markup=nav.adminMenu)


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
        await bot.send_message(message.from_user.id, 'Выберите нужный раздел', reply_markup=nav.infoMenu)
    elif message.text == 'О кормлении':
        await bot.send_message(message.from_user.id, 'Выберите животное', reply_markup=nav.FeedingMenu)
    elif message.text == 'Кормление кошек':
        await bot.send_document(message.chat.id, open(r'files/feed_cats.docx', 'rb'))
    elif message.text == 'Кормление собак':
        await bot.send_document(message.chat.id, open(r'files/feed_dogs.docx', 'rb'))
    elif message.text == 'О вакцинации':
        await bot.send_document(message.chat.id, open(r'files/vaccination.docx', 'rb'))
    elif message.text == 'О содержании':
        await bot.send_document(message.chat.id, open(r'files/maintenance.pdf', 'rb'))
    elif message.text == 'О путешествии с животным':
        await bot.send_message(message.chat.id, 'ссылка на сайт россельхознадзора')

    elif message.text == 'О болезнях':
        await bot.send_message(message.from_user.id, 'В главное меню', reply_markup=nav.DiseaseMenu)
    elif message.text == 'Бешенство':
        await bot.send_document(message.chat.id, open(r'files/rabies.docx', 'rb'))
    elif message.text == 'Лептоспироз':
        await bot.send_document(message.chat.id, open(r'files/lepto.docx', 'rb'))
    elif message.text == 'Стригущий лишай':
        await bot.send_document(message.chat.id, open(r'files/microsporia.docx', 'rb'))
    elif message.text == 'Токсоплазмоз':
        await bot.send_document(message.chat.id, open(r'files/toxoplasmos.docx', 'rb'))
    elif message.text == 'Бабезиоз собак':
        await bot.send_document(message.chat.id, open(r'files/babesios.docx', 'rb'))
    elif message.text == 'Гельминтозы':
        await bot.send_document(message.chat.id, open(r'files/helminthos.docx', 'rb'))
    elif message.text == 'Вирусные инфекции кошек':
        await bot.send_document(message.chat.id, open(r'files/catinfect.docx', 'rb'))
    elif message.text == 'Вирусные инфекции собак':
        await bot.send_document(message.chat.id, open(r'files/doginfect.docx', 'rb'))

    elif message.text == 'Вет услуги':
        await bot.send_message(message.from_user.id, 'Выберите услугу', reply_markup=nav.vetServices)
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'В главное меню', reply_markup=nav.mainMenu)



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_working, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(menu_commands)
