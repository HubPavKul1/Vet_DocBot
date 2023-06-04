import logging
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot, dp

from keyboards.inline.client_kb import *
from states.register import FSMRegAddress
from utils.db import *

logger = logging.getLogger(__name__)


# Регистрация адреса
# @dp.message_handler(Command('Адрес_владельца'), state=None)
async def start_reg_address(message: types.Message):
    await FSMRegAddress.owner_id.set()
    await message.reply('Введите ID владельца', reply_markup=cancel_kb)


# Add owner_id
# @dp.message_handler(state=FSMRegAddress.owner_id)
async def reg_owner(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['owner_id'] = message.text
    await FSMRegAddress.next()
    await message.reply('Введите ID улицы', reply_markup=streets_kb)


# Inline show streets
# @dp.callback_query_handler(state='*', text='streets')
async def show_streets_inline(street: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        streets = show_streets()
        with open(r'files/streets.txt', 'w', encoding='utf8') as file:
            file.write(streets)
    await bot.send_document(street.from_user.id, open(r'files/streets.txt', 'rb'))
    await street.answer()


# Add street_id
# @dp.message_handler(state=FSMRegAddress.street_id)
async def reg_street(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['street_id'] = message.text
    await FSMRegAddress.next()
    await message.reply('Введите номер дома', reply_markup=cancel_kb)


# Add house_number
# @dp.message_handler(state=FSMRegAddress.house)
async def reg_house(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['house'] = message.text
    await FSMRegAddress.next()
    await message.reply('Введите номер квартиры', reply_markup=cancel_kb)


# Add flat
# @dp.message_handler(state=FSMRegAddress.flat)
async def reg_flat(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['flat'] = message.text

        owner_id = int(data.get('owner_id'))
        street_id = int(data.get('street_id'))
        house = str(data.get('house'))
        flat = str(data.get('flat'))

    await message.reply(
        'ID владельца: {}\n'
        'ID улицы: {},\n'
        'дом: {}\n'
        'квартира: {}\n'.format(
            owner_id,
            street_id,
            house,
            flat
        ), reply_markup=add_address_kb
    )


# Add address to DB Inline
# @dp.callback_query_handler(state='*', text='add_address')
async def add_address_inline(address: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        try:
            await add_address(
                owner_id=int(data.get('owner_id')),
                street_id=int(data.get('street_id')),
                house=data.get('house'),
                flat=data.get('flat')
            )
            await address.answer(f"Адрес успешно добавлен в таблицу address", show_alert=True)
            await state.finish()
        except:
            logger.exception()


def register_handlers_admin_reg_address(dp: Dispatcher):
    dp.register_message_handler(start_reg_address, Command('Адрес_владельца'), state=None)
    dp.register_message_handler(reg_owner, state=FSMRegAddress.owner_id)
    dp.register_callback_query_handler(show_streets_inline, state='*', text='streets')
    dp.register_message_handler(reg_street, state=FSMRegAddress.street_id)
    dp.register_message_handler(reg_house, state=FSMRegAddress.house)
    dp.register_message_handler(reg_flat, state=FSMRegAddress.flat)
    dp.register_callback_query_handler(add_address_inline, state='*', text='add_address')
