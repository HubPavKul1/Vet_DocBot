from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


btnMain = KeyboardButton('Главное меню')

# --- Main menu for admin ---

btnDrags = KeyboardButton('Справочник препаратов')
btnCure = KeyboardButton('Схемы лечения')
# btnContact = KeyboardButton('Позвонить врачу')

adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDrags).add(btnCure)


# --- Main menu for clients ---

btnInfo = KeyboardButton('Инфо для владельцев животных')
btnServices = KeyboardButton('Вет услуги')
# btnContact = KeyboardButton('Позвонить врачу')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo).add(btnServices)

# --- Info menu ---

btnDiseases = KeyboardButton('О болезнях')
btnFeeding = KeyboardButton('О кормлении')
btnMaintenance = KeyboardButton('О содержании')
btnVac = KeyboardButton('О вакцинации')
btnTravel = KeyboardButton('О путешествии с животным')

infoMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnDiseases, btnFeeding, btnMaintenance).\
    add(btnVac, btnTravel).add(btnMain)

# --- Vet services ---

btnVaccin = KeyboardButton('Вакцинация')
btnOper = KeyboardButton('Операции')
btnTreatment = KeyboardButton('Лечение')

vetServices = ReplyKeyboardMarkup(resize_keyboard=True).row(btnVaccin, btnOper, btnTreatment).add(btnMain)