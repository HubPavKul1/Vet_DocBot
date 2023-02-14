from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMRegOwner(StatesGroup):
    first_name = State()
    last_name = State()


class FSMRegAddress(StatesGroup):
    owner_id = State()
    street_id = State()
    house = State()
    flat = State()


class FSMRegAnimal(StatesGroup):
    species_id = State()
    breed_id = State()
    sex = State()
    date_of_birth = State()
    nickname = State()
    owner_id = State()


class FSMRegOrder(StatesGroup):
    date = State()
    owner_id = State()
    patient_id = State()
    cost = State()


class FSMAddService(StatesGroup):
    order_id = State()
    service_id = State()
    medication = State()



