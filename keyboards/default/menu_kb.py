from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


btnMain = KeyboardButton('Главное меню')

# --- Main menu for admin ---

btnDrags = KeyboardButton('Справочник препаратов')
btnCure = KeyboardButton('Схемы лечения')
btnInfo = KeyboardButton('Инфо для владельцев животных')
btnServices = KeyboardButton('Вет услуги')

adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDrags).add(btnCure).add(btnInfo).add(btnServices)


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

# --- Feeding menu ---

btnFeedDogs = KeyboardButton('Кормление собак')
btnFeedCats = KeyboardButton('Кормление кошек')

FeedingMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFeedDogs).add(btnFeedCats).add(btnInfo).add(btnMain)

# --- Disease menu ---

btnRabies = KeyboardButton('Бешенство')
btnLeptospirosis = KeyboardButton('Лептоспироз')
btnMicrosporia = KeyboardButton('Стригущий лишай')
btnToxoplasmosis = KeyboardButton('Токсоплазмоз')
btnBabesiosis = KeyboardButton('Бабезиоз собак')
btnHelminthosis = KeyboardButton('Гельминтозы')
btnCatsDisease = KeyboardButton('Вирусные инфекции кошек')
btnDogsDisease = KeyboardButton('Вирусные инфекции собак')

DiseaseMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnRabies, btnLeptospirosis).\
    add(btnMicrosporia, btnToxoplasmosis).add(btnBabesiosis, btnHelminthosis).add(btnCatsDisease, btnDogsDisease).\
    add(btnMain, btnInfo)

