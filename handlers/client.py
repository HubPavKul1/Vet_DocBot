from aiogram import types, Dispatcher

from create_bot import bot, dp
from keyboards.default import menu_kb as nav
from keyboards.inline import client_kb as inl_kb
from data import config
from utils import db

admins = config.ADMINS
contact_phone = config.PHONE
contact_email = config.EMAIL
contact_telegram = config.TELEGRAM
contact_viber = config.VIBER


# @dp.message_handler(commands=['start'])
async def start_working(message: types.Message):
    user_id = message.from_user.id
    if str(user_id) not in admins:
        await bot.send_message(message.from_user.id,
                               'Здравствуйте, {0.first_name}!\n'
                               'Меня зовут Павел.\n'
                               'Я работаю ветеринарным врачом в г.Иваново более 20-ти лет.\n'
                               'Надеюсь, я смогу быть Вам полезен\n'
                               'Выберите необходимую команду в меню'.format(message.from_user),
                               reply_markup=nav.mainMenu)

    else:
        await bot.send_message(message.from_user.id, 'Привет, хозяин! Чего изволишь?',
                               reply_markup=nav.adminMenu)

    if not db.user_exists(user_id=user_id):
        await db.add_user(user_id=user_id,
                          first_name=message.from_user.first_name,
                          last_name=message.from_user.last_name
                          )
        await bot.send_message(config.ADMINS[0], "{0.first_name} {0.last_name} добавлен в таблицу users!".
                               format(message.from_user))
    else:
        await bot.send_message(config.ADMINS[0], "{0.first_name} {0.last_name} подключился к боту!".
                               format(message.from_user))


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите команду в меню для продолжения работы')


@dp.callback_query_handler(text='vet_phone')
async def phone_inline(phone: types.CallbackQuery):
    await phone.message.answer(contact_phone)
    await phone.answer()


@dp.callback_query_handler(text='vet_e-mail')
async def email_inline(email: types.CallbackQuery):
    await email.message.answer(contact_email)
    await email.answer()


@dp.callback_query_handler(text='vet_telegram')
async def telegram_inline(telegram: types.CallbackQuery):
    await telegram.message.answer(contact_telegram)
    await telegram.answer()


@dp.callback_query_handler(text='vet_viber')
async def viber_inline(viber: types.CallbackQuery):
    await viber.message.answer(contact_viber)
    await viber.answer()


# @dp.message_handler(content_types=['text'])
async def menu_commands(message: types.Message):
    if message.text == 'Инфо для владельцев животных':
        await bot.send_message(message.from_user.id, 'Выберите нужный раздел', reply_markup=nav.infoMenu)
        if not db.user_exists(user_id=message.from_user.id):
            await db.add_user(user_id=message.from_user.id,
                              first_name=message.from_user.first_name,
                              last_name=message.from_user.last_name
                              )
            await bot.send_message(config.ADMINS[0], "{0.first_name} {0.last_name} добавлен в таблицу users!".
                                   format(message.from_user))
        else:
            await bot.send_message(config.ADMINS[0], "{0.first_name} {0.last_name} подключился к боту!".
                                   format(message.from_user))

    elif message.text == 'Консультация врача':
        await bot.send_message(message.from_user.id, '{0.first_name}, \n'
                                                     'Вы можете позвонить мне или написать сообщение'.
                               format(message.from_user),
                               reply_markup=inl_kb.contacts_kb
                               )

    elif message.text == 'О кормлении':
        await bot.send_message(message.from_user.id, 'Выберите животное', reply_markup=nav.FeedingMenu)
    elif message.text == 'Кормление кошек':
        await bot.send_document(message.chat.id, open(r'files/feed_cats.docx', 'rb'))
    elif message.text == 'Кормление собак':
        await bot.send_document(message.chat.id, open(r'files/feed_dogs.docx', 'rb'))

    elif message.text == 'О содержании':
        await bot.send_message(message.from_user.id, 'Выберите животное', reply_markup=nav.MaintenanceMenu)
    elif message.text == 'О щенках':
        await bot.send_document(message.chat.id, open(r'files/puppy.docx', 'rb'))
    elif message.text == 'О котятах':
        await bot.send_document(message.chat.id, open(r'files/kitten.docx', 'rb'))
    elif message.text == 'Правила Ивановской области':
        await bot.send_document(message.chat.id, open(r'files/maintenance.pdf', 'rb'))

    elif message.text == 'О вакцинации':
        await bot.send_document(message.chat.id, open(r'files/vaccination.docx', 'rb'))

    elif message.text == 'О путешествии с животным':
        await bot.send_message(message.chat.id,
                               'https://fsvps.gov.ru/fsvps/importExport/pets/instructionExportPets.html')

    elif message.text == 'О болезнях':
        await bot.send_message(message.from_user.id, 'Выберите заболевание', reply_markup=nav.DiseaseMenu)

    elif message.text == 'Заразные болезни':
        await bot.send_message(message.from_user.id, 'Выберите заболевание', reply_markup=nav.InfMenu)
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

    elif message.text == 'Незаразные болезни':
        await bot.send_message(message.from_user.id, 'Выберите заболевание', reply_markup=nav.UninfMenu)
    elif message.text == 'Урологические проблемы кошек':
        await bot.send_document(message.chat.id, open(r'files/urology.docx', 'rb'))
    elif message.text == 'Болезни кожи':
        await bot.send_document(message.chat.id, open(r'files/dermatology.docx', 'rb'))

    elif message.text == 'Вет услуги':
        await bot.send_message(message.from_user.id, 'Выберите услугу', reply_markup=nav.vetServices)
    elif message.text == 'Вакцинация':
        await bot.send_message(message.from_user.id, 'Выезд и вакцинация животного: \n'
                                                     'отечественной вакциной - 2000 руб.,\n'
                                                     'импортной вакциной - 2500 руб.',
                               reply_markup=inl_kb.contacts_kb
                               )
    elif message.text == 'Операции':
        await bot.send_message(message.from_user.id, 'Кастрация кота - 2000 руб.,\n'
                                                     'Стерилизация кошки - 3000 руб.,\n'
                                                     'Простые хирургические операции '
                                                     '(хирургическая обработка ран, '
                                                     'вскрытие абцессов и т.п) - 2000 руб.,\n'
                                                     'Сложные хирургические операции - 3000',
                               reply_markup=inl_kb.contacts_kb
                               )
    elif message.text == 'Лечение':
        await bot.send_message(message.from_user.id, 'Выезд и лечение животного: \n'
                                                     'с легкой патологией - 2000 руб.,\n'
                                                     'c патологией средней тяжести - 2500 руб.,\n'
                                                     'при тяжелой патологии - 3000 руб.',
                               reply_markup=inl_kb.contacts_kb
                               )

    elif message.text == 'Мочекаменная болезнь':
        await bot.send_message(message.from_user.id, 'Выезд и лечение котов с острой задержкой мочи: \n'
                                                     'без капельницы - 2000 руб.,\n'
                                                     'с капельницей - 3000 руб.',
                               reply_markup=inl_kb.contacts_kb
                               )
    elif message.text == 'Послеоперационный уход':
        await bot.send_document(message.chat.id, open(r'files/postoperative_care.docx', 'rb'))

    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'В главное меню', reply_markup=nav.mainMenu)

    elif message.text == 'Админка':
        await bot.send_message(message.from_user.id, 'Администратор', reply_markup=nav.vetHelp)
    elif message.text == 'Регистрация':
        await bot.send_message(message.from_user.id, 'Регистрация', reply_markup=nav.vetReg)
    elif message.text == 'Справочник препаратов':
        await bot.send_message(message.from_user.id, 'Справочник препаратов', reply_markup=nav.vetDrugs)
    elif message.text == 'Список препаратов':
        await bot.send_document(message.chat.id, open(r'vet_parser/drugs.json', 'rb'))
    else:
        await bot.send_message(message.from_user.id, 'Не понял команду {}, выберите услугу или нажмите /start'
                               .format(message.from_user.first_name))


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_working, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(menu_commands, content_types=['text'])
