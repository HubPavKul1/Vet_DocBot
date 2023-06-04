from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- Contacts Inline ---
phone_btn = InlineKeyboardButton(text='телефон врача', callback_data='vet_phone')
e_mail_btn = InlineKeyboardButton(text='e-mail', callback_data='vet_e-mail')
telegram_btn = InlineKeyboardButton(text='telegram', callback_data='vet_telegram')
viber_btn = InlineKeyboardButton(text='viber', callback_data='vet_viber')
contacts_kb = InlineKeyboardMarkup(row_width=3).add(phone_btn, telegram_btn, e_mail_btn)

# --- Cancel Inline for Register ---
cancel_btn = InlineKeyboardButton(text='отмена', callback_data='cancel')
cancel_kb = InlineKeyboardMarkup().add(cancel_btn)

# --- Species Inline for Register
dog_btn = InlineKeyboardButton(text='собака 1', callback_data='1')
cat_btn = InlineKeyboardButton(text='кошка 2', callback_data='2')
animal_kb = InlineKeyboardMarkup(row_width=2).add(dog_btn, cat_btn).add(cancel_btn)

# --- Sex Inline for Register ---
male_btn = InlineKeyboardButton(text='м', callback_data='male')
female_btn = InlineKeyboardButton(text='ж', callback_data='female')
sex_kb = InlineKeyboardMarkup(row_width=2).add(male_btn, female_btn).add(cancel_btn)

# --- Add_patient Inline to DB ---
add_patient_btn = InlineKeyboardButton(text='добавить пациента в БД', callback_data='add_patient')
add_patient_kb = InlineKeyboardMarkup().add(add_patient_btn, cancel_btn)

# --- Show breed Inline for Register ---
breed_btn = InlineKeyboardButton(text='показать породы', callback_data='breeds')
breed_kb = InlineKeyboardMarkup(row_width=2).add(breed_btn, cancel_btn)

# --- Show streets Inline for Register ---
streets_btn = InlineKeyboardButton(text='показать улицы', callback_data='streets')
streets_kb = InlineKeyboardMarkup(row_width=2).add(streets_btn, cancel_btn)

# --- Add_address Inline to DB ---
add_address_btn = InlineKeyboardButton(text='добавить адрес в БД', callback_data='add_address')
add_address_kb = InlineKeyboardMarkup().add(add_address_btn, cancel_btn)

# --- Show owners Inline for Register ---
owners_btn = InlineKeyboardButton(text='показать владельцев', callback_data='owners')
owners_kb = InlineKeyboardMarkup(row_width=2).add(owners_btn, cancel_btn)

# --- Show users Inline for Register ---
users_btn = InlineKeyboardButton(text='показать users', callback_data='users')
users_kb = InlineKeyboardMarkup(row_width=2).add(users_btn, cancel_btn)

# --- Show patients Inline for Register ---
patients_btn = InlineKeyboardButton(text='показать пациентов', callback_data='patients')
patients_kb = InlineKeyboardMarkup(row_width=2).add(patients_btn, cancel_btn)

# --- Add_order Inline to DB ---
add_order_btn = InlineKeyboardButton(text='добавить заказ в БД', callback_data='add_order')
add_order_kb = InlineKeyboardMarkup().add(add_order_btn, cancel_btn)

# --- Add_owner Inline to DB ---
add_owner_btn = InlineKeyboardButton(text='добавить владельца в БД', callback_data='add_owner')
add_owner_kb = InlineKeyboardMarkup().add(add_owner_btn, cancel_btn)

# --- Show price Inline for Register ---
price_btn = InlineKeyboardButton(text='показать прайс', callback_data='price')
price_kb = InlineKeyboardMarkup(row_width=2).add(price_btn, cancel_btn)

# --- Add service and treatment Inline to DB ---
add_service_btn = InlineKeyboardButton(text='добавить услугу в заказ', callback_data='add_service')
add_treatment_btn = InlineKeyboardButton(text='добавить лечение в заказ', callback_data='add_treatment')
add_to_order_kb = InlineKeyboardMarkup(row_width=2).add(add_service_btn, add_treatment_btn, cancel_btn)

# --- Search drug by name Inline ---
search_drug_btn = InlineKeyboardButton(text='найти препарат', callback_data='search_drug')
search_drug_kb = InlineKeyboardMarkup().add(search_drug_btn, cancel_btn)

