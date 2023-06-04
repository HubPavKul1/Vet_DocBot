from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types, Dispatcher
from create_bot import bot, dp
from vet_parser.site_parser import *

from keyboards.inline.client_kb import *
from states.register import FSMSearchDrug


async def start_search_drug(message: types.Message):
    await FSMSearchDrug.drug_name.set()
    await message.reply('Введите наименование препарата', reply_markup=cancel_kb)


async def set_drug_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['drug_name'] = message.text
    await message.reply('Поиск', reply_markup=search_drug_kb)


async def search_drug_inline(search_drug: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        drug_name = data.get('drug_name')
        drug = search_drug_by_name(drug_name)
        if len(drug) == 1:
            if isinstance(drug[0], str):
                await search_drug.answer(drug[0], show_alert=True)
            else:
                with open('drug.txt', 'w', encoding='utf-8') as f:
                    f.write(drug[0]['description'])
                await search_drug.message.answer(drug[0]['title'])
                await search_drug.message.answer(drug[0]['image'])
                await bot.send_document(search_drug.from_user.id, open('drug.txt', 'rb'))
                await search_drug.answer()
        elif len(drug) > 1:
            for item in drug:
                with open('drug.txt', 'w', encoding='utf-8') as f:
                    f.write(item['description'])
                await search_drug.message.answer(item['title'])
                await search_drug.message.answer(item['image'])
                await bot.send_document(search_drug.from_user.id, open('drug.txt', 'rb'))
                await search_drug.answer()
    await state.finish()


def register_handlers_search_drug(dp: Dispatcher):
    dp.register_message_handler(start_search_drug, Command('Поиск_препарата'), state=None)
    dp.register_message_handler(set_drug_name, state=FSMSearchDrug.drug_name)
    dp.register_callback_query_handler(search_drug_inline, state='*', text='search_drug')


