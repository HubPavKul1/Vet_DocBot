from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot, dp

from keyboards.inline.client_kb import *
from states.register import FSMRegAnimal
from utils.db import *


# Регистрация животного
# @dp.message_handler(Command('Регистрация_животного'), state=None)
async def start_reg_animal(message: types.Message):
    await FSMRegAnimal.species_id.set()
    await message.reply('Выберите вид животного', reply_markup=animal_kb)


# Inline Dog
# @dp.callback_query_handler(state=FSMRegAnimal.species_id, text='1')
async def dog_inline(dog: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['species_id'] = '1'
    await FSMRegAnimal.next()
    await dog.message.answer('Введите ID породы животного', reply_markup=breed_kb)
    await dog.answer()


# Inline Cat
# @dp.callback_query_handler(state=FSMRegAnimal.species_id, text='2')
async def cat_inline(cat: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['species_id'] = '2'
    await FSMRegAnimal.next()
    await cat.message.answer('Введите ID породы животного', reply_markup=breed_kb)
    await cat.answer()


# Inline show breeds
# @dp.callback_query_handler(state='*', text='breeds')
async def show_breeds_inline(breed: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        species_id = int(data.get('species_id'))
        breeds = show_breeds(species_id)
        with open(r'files/breeds.txt', 'w', encoding='utf8') as file:
            file.write(breeds)
    await bot.send_document(breed.from_user.id, open(r'files/breeds.txt', 'rb'))
    await breed.answer()


# Отмена регистрации
# @dp.callback_query_handler(state='*', text='cancel')
async def cancel_handler(cancel: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await cancel.message.answer('OK')
    await cancel.answer()


# Add breed_id and choose sex
# @dp.message_handler(state=FSMRegAnimal.breed_id)
async def reg_breed(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['breed_id'] = message.text
    await FSMRegAnimal.next()
    await message.reply('Выберите пол животного', reply_markup=sex_kb)


# Male Inline
# @dp.callback_query_handler(state=FSMRegAnimal.sex, text='male')
async def male_inline(male: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['sex'] = 'м'
    await FSMRegAnimal.next()
    await male.message.answer('Введите дату рождения в форме гггг-мм-дд', reply_markup=cancel_kb)
    await male.answer()


# Female Inline
# @dp.callback_query_handler(state=FSMRegAnimal.sex, text='female')
async def female_inline(female: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['sex'] = 'ж'
    await FSMRegAnimal.next()
    await female.message.answer('Введите дату рождения в форме гггг-мм-дд', reply_markup=cancel_kb)
    await female.answer()


# Add date of birth
# @dp.message_handler(state=FSMRegAnimal.date_of_birth)
async def reg_date_of_birth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_of_birth'] = message.text
    await FSMRegAnimal.next()
    await message.reply('Введите кличку животного', reply_markup=cancel_kb)


# Add nickname
# @dp.message_handler(state=FSMRegAnimal.nickname)
async def reg_nickname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
    await FSMRegAnimal.next()
    await message.reply('Введите ID владельца животного', reply_markup=cancel_kb)


# Add user_id
# @dp.message_handler(state=FSMRegAnimal.owner_id)
async def reg_owner(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['owner_id'] = message.text

        species_id = int(data.get('species_id'))
        breed_id = int(data.get('breed_id'))
        sex = str(data.get('sex'))
        date_of_birth = str(data.get('date_of_birth'))
        nickname = str(data.get('nickname'))
        owner_id = int(data.get('owner_id'))
    await message.reply(
        'ID животного: {}\n'
        'ID породы: {},\n'
        'пол: {}\n'
        'дата рождения: {}\n'
        'кличка: {}\n'
        'ID владельца: {}'.format(
            species_id,
            breed_id,
            sex,
            date_of_birth,
            nickname,
            owner_id
        ), reply_markup=add_patient_kb
    )


# Add patient to DB Inline
# @dp.callback_query_handler(state='*', text='add_patient')
async def add_patient_inline(patient: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await add_patient(
            species_id=int(data.get('species_id')),
            breed_id=int(data.get('breed_id')),
            sex=data.get('sex'),
            date_of_birth=data.get('date_of_birth'),
            nickname=data.get('nickname'),
            owner_id=int(data.get('owner_id'))
        )
    await patient.answer(f"Пациент {data.get('nickname')}\n успешно добавлен(a) в таблицу patient", show_alert=True)

    await state.finish()


def register_handlers_admin_reg_patient(dp: Dispatcher):
    dp.register_message_handler(start_reg_animal, Command('Регистрация_животного'), state=None)
    dp.register_callback_query_handler(cancel_handler, state='*', text='cancel')
    dp.register_callback_query_handler(dog_inline, state=FSMRegAnimal.species_id, text='1')
    dp.register_callback_query_handler(cat_inline, state=FSMRegAnimal.species_id, text='2')
    dp.register_callback_query_handler(show_breeds_inline, state='*', text='breeds')
    dp.register_message_handler(reg_breed, state=FSMRegAnimal.breed_id)
    dp.register_callback_query_handler(male_inline, state=FSMRegAnimal.sex, text='male')
    dp.register_callback_query_handler(female_inline, state=FSMRegAnimal.sex, text='female')
    dp.register_message_handler(reg_date_of_birth, state=FSMRegAnimal.date_of_birth)
    dp.register_message_handler(reg_nickname, state=FSMRegAnimal.nickname)
    dp.register_message_handler(reg_owner, state=FSMRegAnimal.owner_id)
    dp.register_callback_query_handler(add_patient_inline, state='*', text='add_patient')
