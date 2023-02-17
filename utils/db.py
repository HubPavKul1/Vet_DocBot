import psycopg2 as ps
from psycopg2 import Error
from data.config import DATABASE_URL

from .sql_queries import *


# try:
#     connection = ps.connect(DATABASE_URL)
#     cur = connection.cursor()
#     print('Подключение к БД')
#     print("Информация о сервере PostgreSQL")
#     print(connection.get_dsn_parameters(), "\n")
# except (Exception, Error) as error:
#     print("Ошибка при работе с PostgreSQL", error)
# finally:
#     if connection:
#         cur.close()
#         connection.close()
#         print("Соединение с PostgreSQL закрыто")
def create_tables() -> None:
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(create_tables_query)


def user_exists(user_id: int) -> bool:
    """Check user exists in db"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(user_exists_query, (user_id,))
            result = cursor.fetchone()
            return bool(result)


def get_user_id(user_id: int) -> int:
    """Get user from db by user_id"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(get_user_id_query, (user_id,))
            result = cursor.fetchone()
            return result[0]


def add_user(user_id: int, first_name: str, last_name: str) -> None:
    """Add user to db"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(add_user_query, (user_id, first_name, last_name))
            return conn.commit()


def get_streets(street: str):
    """Get streets from table streets"""
    street = '%{}%'.format(street).title()

    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(get_streets_query, (street,))
            result = cursor.fetchall()
            return result


def get_street_id(street: str) -> int:
    """Get street id from db"""
    street = '%{}%'.format(street).title()
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(get_street_id, (street,))
            result = cursor.fetchone()
            return result[0]


def get_species_id(species: str) -> int:
    """Get species id from db"""
    species = '%{}%'.format(species).lower()
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(get_species_id_query, (species,))
            result = cursor.fetchone()[0]
            return result


def get_breed_id(species_id: int, breed: str) -> int:
    """Get breed id from db"""
    breed = '{}%'.format(breed).capitalize()
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(get_breed_id_query, (species_id, breed))
            result = cursor.fetchone()[0]
            return result


def get_service_id(service: str) -> int:
    """Get service id from db"""
    service = '%{}%'.format(service)
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(get_service_id_query, (service,))
            result = cursor.fetchone()
            return result[0]


def show_users() -> str:
    """Get user id, first_name, last_name from db"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(show_users_query)
            result = cursor.fetchall()
            users = ''
            for item in result:
                users += f'{item[1]} {item[2]}: {item[0]}' + '\n'
            return users


# --- Регистрация заказа ---
# --- Регистрация владельца ---
async def add_owner(first_name: str, last_name: str):
    """Add owner to db"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(add_owner_query, (first_name, last_name))
            return conn.commit()


def show_streets() -> str:
    """Get street id, name from db"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(show_streets_query)
            result = cursor.fetchall()
            streets = ''
            for item in result:
                streets += f'{item[1]}: {item[0]}' + '\n'
            return streets


# --- Регистрация адреса ---
async def add_address(owner_id: int, street_id: int, house: str, flat: int):
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(add_address_query, (owner_id, street_id, house, flat))
            return conn.commit()


# --- Регистрация пациента ---
def show_breeds(species_id: int) -> str:
    """Get breed id, name from db"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(""" SELECT * FROM breeds WHERE species_id = %s """, (species_id,))
            result = cursor.fetchall()
            breed_string = ''
            for item in result:
                breed_string += f'{item[1]}: {item[0]}' + '\n'
            return breed_string


async def add_patient(species_id: int, breed_id: int, sex: str, date_of_birth: str, nickname: str, owner_id: int):
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(""" INSERT INTO patients (
                            species_id,
                            breed_id,
                            sex,
                            date_of_birth,
                            nickname,
                            owner_id       
                            )
                            VALUES (
                            %s, %s, %s, %s, %s, %s
                            )
                            """, (
                species_id,
                breed_id,
                sex,
                date_of_birth,
                nickname,
                owner_id
            ))
            return conn.commit()


# --- Регистрация заказа
def show_owners() -> str:
    """Get owner id, first_name, last_name from db"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(""" SELECT id, first_name, last_name FROM owners ORDER BY id DESC """)
            result = cursor.fetchall()
            owners = ''
            for item in result:
                owners += f'{item[1]} {item[2]}: {item[0]}' + '\n'
            return owners


def show_patients() -> str:
    """Show patients"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(""" 
            SELECT  
            species.name, 
            breeds.name, 
            patients.nickname, 
            patients.id
            FROM patients 
            JOIN species ON species.id = patients.species_id
            JOIN breeds ON breeds.id = patients.breed_id
            ORDER BY patients.id DESC 
            """)
            result = cursor.fetchall()
            patients = ''
            for item in result:
                patients += f'{item[0]} {item[1]} {item[2]}: {item[3]}' + '\n'
            return patients


async def add_order(date: str, owner_id: int, patient_id: int, cost: int):
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(""" INSERT INTO orders (
                            date,
                            owner_id,
                            patient_id,
                            cost
                            )
                            VALUES (
                            %s, %s, %s, %s
                            )
                            """, (
                date,
                owner_id,
                patient_id,
                cost
            ))
            return conn.commit()


# --- Добавление услуги к заказу ---
def show_price() -> str:
    """Get service id, name from db"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(""" SELECT service, price, id FROM vet_service """)
            result = cursor.fetchall()
            services = ''
            for item in result:
                services += f'{item[0]}; цена: {item[1]} руб.; ID: {item[2]}' + '\n'
            return services


async def add_service(order_id, service_id):
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(""" INSERT INTO order_service (
                            order_id,
                            service_id
                            )
                            VALUES (
                            %s, %s
                            )
                            """, (
                order_id,
                service_id

            ))
            return conn.commit()


async def add_treatment(order_id, medication):
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(""" INSERT INTO order_treatment (
                            order_id,
                            medication
                            )
                            VALUES (
                            %s, %s
                            )
                            """, (
                order_id,
                medication

            ))
            return conn.commit()


# --- SHOW REGISTER ---
def show_register() -> str:
    """Show register"""
    with ps.connect(DATABASE_URL, sslmode='require') as conn:
        with conn.cursor() as cursor:
            cursor.execute(""" 
            SELECT  
            orders.date,
            owners.last_name,
            owners.first_name,
            species.name,
            breeds.name,
            patient.date_of_birth,  
            patient.nickname,
            vet_service.service,
            order_treatment.medication,
            orders.cost
            FROM orders 
            JOIN owners ON owners.id = orders.owner_id
            JOIN patient ON patient.id = orders.patient_id
            JOIN species ON species.id = patient.species_id
            JOIN breeds ON breeds.id = patient.breed_id
            LEFT JOIN order_service ON orders.id = order_service.order_id
            JOIN vet_service ON vet_service.id = order_service.service_id
            LEFT JOIN order_treatment ON orders.id = order_treatment.order_id  
            ORDER BY orders.date DESC     
            """)
            result = cursor.fetchall()
            rows = ''

            for item in result:
                rows += f'| {item[0]} | {item[1]} | {item[2]} | {item[3]} | ' \
                            f'{item[4]} | {item[5]} | {item[6]} | {item[7]} | {item[8]} | {item[9]} |' + '\n'
            return rows
