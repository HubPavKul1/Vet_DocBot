from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types, Dispatcher
from create_bot import bot, dp

from keyboards.inline.client_kb import *
from states.register import FSMRegOwner
from utils.db import *


# Регистрация владельца
# @dp.message_handler(Command('Регистрация_владельца'), state=None)
async def start_reg_owner(message: types.Message):
    await FSMRegOwner.first_name.set()
    await message.reply('Введите имя владельца', reply_markup=cancel_kb)


# @dp.message_handler(state=FSMRegOwner.first_name)
async def reg_first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await FSMRegOwner.next()
    await message.reply('Введите фамилию владельца', reply_markup=cancel_kb)


# @dp.message_handler(state=FSMRegOwner.last_name)
async def reg_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text

        first_name = str(data.get('first_name'))
        last_name = str(data.get('last_name'))

    await message.reply(
        'имя владельца: {}\n'
        'фамилия владельца: {}\n'.format(
            first_name,
            last_name
        ), reply_markup=add_owner_kb
    )


# Add owner to DB Inline
# @dp.callback_query_handler(state='*', text='add_owner')
async def add_owner_inline(owner: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await add_owner(
            first_name=data.get('first_name'),
            last_name=data.get('last_name')
        )
    await owner.answer(f"Владелец успешно добавлен в таблицу owners", show_alert=True)

    await state.finish()


# @dp.callback_query_handler(text='users')
async def show_users_inline(user: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        users = show_users()
        with open(r'files/users.txt', 'w', encoding='utf8') as file:
            file.write(users)
    await bot.send_document(user.from_user.id, open(r'files/users.txt', 'rb'))
    await user.answer()


def register_handlers_admin_reg_owner(dp: Dispatcher):
    dp.register_message_handler(start_reg_owner, Command('Регистрация_владельца'), state=None)
    dp.register_message_handler(reg_first_name, state=FSMRegOwner.first_name)
    dp.register_message_handler(reg_last_name, state=FSMRegOwner.last_name)
    dp.register_callback_query_handler(show_users_inline, text='users')
    dp.register_callback_query_handler(add_owner_inline, state='*', text='add_owner')
