from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


btnMain = KeyboardButton('Главное меню')

# --- Main menu for admin ---
btnAdmin = KeyboardButton('Админка')
btnInfo = KeyboardButton('Инфо для владельцев животных')
btnServices = KeyboardButton('Вет услуги')

adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAdmin).add(btnInfo).add(btnServices)


# --- Next menu for admin ---
btnDrags = KeyboardButton('Справочник препаратов')
btnCure = KeyboardButton('Схемы лечения')
btnRegister = KeyboardButton('Регистрация')

vetHelp = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDrags, btnCure).add(btnRegister).add(btnMain)

# --- Register menu for admin ---
btnOwner = KeyboardButton('/Регистрация_владельца')
btnShowOwners = KeyboardButton('/Владельцы_животных')
btnAddress = KeyboardButton('/Адрес_владельца')
btnPatient = KeyboardButton('/Регистрация_животного')
btnOrder = KeyboardButton('/Регистрация_заказа')
btnToOrder = KeyboardButton('/Добавить_услугу')
btnWorkRegister = KeyboardButton('/Журнал_регистрации')

vetReg = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOwner).add(btnShowOwners).add(btnPatient).add(btnAddress).\
    add(btnOrder).add(btnToOrder).add(btnWorkRegister).add(btnMain)


# --- Main menu for clients ---

btnInfo = KeyboardButton('Инфо для владельцев животных')
btnServices = KeyboardButton('Вет услуги')
btnContacts = KeyboardButton('Консультация врача')


mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo).add(btnServices).add(btnContacts)

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
btnUri = KeyboardButton('Мочекаменная болезнь')
btnPostOper = KeyboardButton('Послеоперационный уход')

vetServices = ReplyKeyboardMarkup(resize_keyboard=True).row(btnVaccin, btnOper, btnTreatment).\
    add(btnUri).add(btnPostOper).add(btnMain)

# --- Feeding menu ---

btnFeedDogs = KeyboardButton('Кормление собак')
btnFeedCats = KeyboardButton('Кормление кошек')

FeedingMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFeedDogs, btnFeedCats).add(btnInfo, btnMain)

# --- Maintenance menu ---

btnPuppy = KeyboardButton('О щенках')
btnKitten = KeyboardButton('О котятах')
btnRules = KeyboardButton('Правила Ивановской области')

MaintenanceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPuppy, btnKitten).add(btnRules).add(btnInfo, btnMain)

# --- Disease menu ---

btnInfec = KeyboardButton('Заразные болезни')
btnUninfec = KeyboardButton('Незаразные болезни')

DiseaseMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnInfec, btnUninfec).add(btnMain, btnInfo)

# --- Infectious menu ---

btnRabies = KeyboardButton('Бешенство')
btnLeptospirosis = KeyboardButton('Лептоспироз')
btnMicrosporia = KeyboardButton('Стригущий лишай')
btnToxoplasmosis = KeyboardButton('Токсоплазмоз')
btnBabesiosis = KeyboardButton('Бабезиоз собак')
btnHelminthosis = KeyboardButton('Гельминтозы')
btnCatsDisease = KeyboardButton('Вирусные инфекции кошек')
btnDogsDisease = KeyboardButton('Вирусные инфекции собак')

InfMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnRabies, btnLeptospirosis, btnMicrosporia).\
    add(btnToxoplasmosis,btnBabesiosis, btnHelminthosis).add(btnCatsDisease, btnDogsDisease).\
    add(btnMain, btnDiseases)

# --- Uninfectious menu ---

btnUrologic = KeyboardButton('Урологические проблемы кошек')
btnDerm = KeyboardButton('Болезни кожи')
UninfMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnUrologic).add(btnDerm).add(btnMain, btnDiseases)


