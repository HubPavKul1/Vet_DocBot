from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    photo = State()
    disease = State()
    service = State()
    description = State()
    price = State()



