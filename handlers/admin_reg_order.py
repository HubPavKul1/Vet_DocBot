from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot, dp

from keyboards.inline.client_kb import *
from states.register import FSMRegOrder, FSMAddService
from utils.db import *


# Регистрация заказа
# @dp.message_handler(Command('Регистрация_заказа'), state=None)
async def start_reg_order(message: types.Message):
    await FSMRegOrder.date.set()
    await message.reply('Введите дату заказа в форме гггг-мм-дд', reply_markup=cancel_kb)


# @dp.message_handler(state=FSMRegOrder.date)
async def reg_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await FSMRegOrder.next()
    await message.reply('Введите ID владельца', reply_markup=owners_kb)


# @dp.callback_query_handler(state='*', text='users')
async def show_owners_inline(owner: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        owners = show_owners()
        with open(r'files/owners.txt', 'w', encoding='utf8') as file:
            file.write(owners)
    await bot.send_document(owner.from_user.id, open(r'files/owners.txt', 'rb'))
    await owner.answer()


# @dp.message_handler(state=FSMRegOrder.owner_id)
async def reg_owner(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['owner_id'] = message.text
    await FSMRegOrder.next()
    await message.reply('Введите ID пациента', reply_markup=patients_kb)


# @dp.callback_query_handler(state='*', text='patients')
async def show_patients_inline(patient: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        patients = show_patients()
        with open(r'files/patients.txt', 'w', encoding='utf8') as file:
            file.write(patients)
    await bot.send_document(patient.from_user.id, open(r'files/patients.txt', 'rb'))
    await patient.answer()


# @dp.message_handler(state=FSMRegOrder.patient_id)
async def reg_patient(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['patient_id'] = message.text
    await FSMRegOrder.next()
    await message.reply('Введите стоимость заказа, руб.', reply_markup=cancel_kb)


# @dp.message_handler(state=FSMRegOrder.cost)
async def reg_cost(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cost'] = message.text

        date = str(data.get('date'))
        owner_id = int(data.get('owner_id'))
        patient_id = int(data.get('patient_id'))
        cost = float(data.get('cost'))

    await message.reply(
        'дата заказа: {}\n'
        'ID владельца: {}\n'
        'ID пациента: {},\n'
        'стоимость: {}\n'.format(
            date,
            owner_id,
            patient_id,
            cost
        ), reply_markup=add_order_kb
    )


# Add order to DB Inline
# @dp.callback_query_handler(state='*', text='add_order')
async def add_order_inline(address: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await add_order(
            date=data.get('date'),
            owner_id=int(data.get('owner_id')),
            patient_id=int(data.get('patient_id')),
            cost=float(data.get('cost'))
        )
    await address.answer(f"Заказ успешно добавлен в таблицу orders", show_alert=True)

    await state.finish()


# --- Add service to order ---
# @dp.message_handler(Command('Добавить_услугу'), state=None)
async def start_add_service(message: types.Message):
    await FSMAddService.order_id.set()
    await message.reply('Введите ID заказа', reply_markup=cancel_kb)


# @dp.message_handler(state=FSMAddService.order_id)
async def add_order_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['order_id'] = message.text
    await FSMAddService.next()
    await message.reply('Введите ID услуги', reply_markup=price_kb)


# @dp.callback_query_handler(state='*', text='price')
async def show_price_inline(price: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        services = show_price()
        with open(r'files/price.txt', 'w', encoding='utf8') as file:
            file.write(services)
    await bot.send_document(price.from_user.id, open(r'files/price.txt', 'rb'))
    await price.answer()


# @dp.message_handler(state=FSMAddService.service_id)
async def add_service_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['service_id'] = message.text
    await FSMAddService.next()
    await message.reply('Введите лечебные процедуры', reply_markup=cancel_kb)


# @dp.message_handler(state=FSMAddService.medication)
async def add_medication(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['medication'] = message.text

        order_id = int(data.get('order_id'))
        service_id = int(data.get('service_id'))
        medication = str(data.get('medication'))

    await message.reply(
        'ID заказа: {}\n'
        'ID услуги: {}\n'
        'Лечение: {},\n'.format(
            order_id,
            service_id,
            medication
        ), reply_markup=add_to_order_kb
    )


# @dp.callback_query_handler(state='*', text='add_service')
async def add_service_inline(address: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await add_service(
            order_id=int(data.get('order_id')),
            service_id=int(data.get('service_id'))
        )
    await address.answer(f"Услуга успешно добавлена в таблицу order_service", show_alert=True)


# @dp.callback_query_handler(state='*', text='add_treatment')
async def add_treatment_inline(address: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await add_treatment(
            order_id=int(data.get('order_id')),
            medication=data.get('medication')
        )
    await address.answer(f"Лечение успешно добавлено в таблицу order_treatment", show_alert=True)

    await state.finish()


@dp.message_handler(Command('Журнал_регистрации'))
async def show_register_command(message: types.Message):
    rows = show_register()
    with open(r'files/register.txt', 'w', encoding='utf8') as file:
        file.write(rows)
    await bot.send_document(message.from_user.id, open(r'files/register.txt', 'rb'))


def register_handlers_admin_reg_order(dp: Dispatcher):
    dp.register_message_handler(start_reg_order, Command('Регистрация_заказа'), state=None)
    dp.register_message_handler(reg_date, state=FSMRegOrder.date)
    dp.register_callback_query_handler(show_owners_inline, state='*', text='owners')
    dp.register_message_handler(reg_owner, state=FSMRegOrder.owner_id)
    dp.register_callback_query_handler(show_patients_inline, state='*', text='patients')
    dp.register_message_handler(reg_patient, state=FSMRegOrder.patient_id)
    dp.register_message_handler(reg_cost, state=FSMRegOrder.cost)
    dp.register_callback_query_handler(add_order_inline, state='*', text='add_order')

    dp.register_message_handler(start_add_service, Command('Добавить_услугу'), state=None)
    dp.register_message_handler(add_order_id, state=FSMAddService.order_id)
    dp.register_callback_query_handler(show_price_inline, state='*', text='price')
    dp.register_message_handler(add_service_id, state=FSMAddService.service_id)
    dp.register_message_handler(add_medication, state=FSMAddService.medication)
    dp.register_callback_query_handler(add_service_inline, state='*', text='add_service')
    dp.register_callback_query_handler(add_treatment_inline, state='*', text='add_treatment')

    dp.register_message_handler(show_register_command, Command('Журнал_регистрации'))
