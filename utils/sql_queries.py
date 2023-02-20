tables = ['users', 'address', 'patients', 'order_treatment',
          'order_service', 'orders', 'owners', 'streets',
          'breeds', 'species', 'cities', 'vet_service']


create_tables_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    user_id BIGINT,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(250)
);

CREATE TABLE IF NOT EXISTS streets (
    id SERIAL PRIMARY KEY,
    city_id INTEGER REFERENCES cities(id) ON DELETE CASCADE,
    name VARCHAR(250)
);

CREATE TABLE IF NOT EXISTS address (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES owners(id) ON DELETE CASCADE,
    street_id INTEGER REFERENCES streets(id) ON DELETE CASCADE,
    house VARCHAR(10),
    flat INTEGER
);

CREATE TABLE IF NOT EXISTS species (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS breeds (
    id SERIAL PRIMARY KEY,
    species_id INTEGER REFERENCES species(id) ON DELETE CASCADE,
    name VARCHAR(250)
);

CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    species_id INTEGER REFERENCES species(id) ON DELETE CASCADE,
    breed_id INTEGER REFERENCES breeds(id) ON DELETE CASCADE,
    sex VARCHAR(1),
    date_of_birth VARCHAR(20),
    nickname VARCHAR(50), 
    owner_id INTEGER REFERENCES owners(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    order_date VARCHAR(20),
    owner_id INTEGER REFERENCES owners(id) ON DELETE CASCADE,
    patient_id INTEGER,
    cost INTEGER 
);

CREATE TABLE IF NOT EXISTS vet_service (
    id SERIAL PRIMARY KEY,
    service VARCHAR(200),
    price INTEGER
);

CREATE TABLE IF NOT EXISTS order_service (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    service_id INTEGER REFERENCES vet_service(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS order_treatment (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    medication TEXT
);
"""


user_exists_query = """SELECT user_id FROM users WHERE user_id = %s;"""
get_user_id_query = """SELECT id FROM users WHERE user_id = %s;"""
add_user_query = """INSERT INTO users (user_id, first_name, last_name) VALUES (%s, %s, %s);"""
show_users_query = """SELECT * FROM users ORDER BY id DESC;"""

get_streets_query = """SELECT id, name FROM streets WHERE name LIKE %s;"""
get_street_id_query = """SELECT id FROM streets WHERE name LIKE %s;"""
get_city_id_query = """SELECT id FROM cities WHERE name LIKE %s;"""
add_city_query = """INSERT INTO cities (name) VALUES (%s);"""
add_street_query = """INSERT INTO streets (city_id, name) VALUES (%s, %s);"""
show_streets_query = """SELECT id, name FROM streets;"""
add_address_query = """INSERT INTO address (owner_id, street_id, house, flat) VALUES (%s, %s, %s, %s);"""

add_owner_query = """INSERT INTO owners (first_name, last_name) VALUES (%s, %s);"""
show_owners_query = """SELECT id, first_name, last_name FROM owners ORDER BY id DESC;"""
show_patients_query = """
SELECT species.name, breeds.name, patients.nickname, patients.id 
FROM patients 
JOIN species 
ON species.id = patients.species_id 
JOIN breeds 
ON breeds.id = patients.breed_id 
ORDER BY patients.id DESC;
"""

add_order_query = """INSERT INTO orders (order_date, owner_id, patient_id, cost) VALUES (%s, %s, %s, %s);"""
show_price_query = """SELECT service, price, id FROM vet_service;"""
get_service_id_query = """SELECT id FROM vet_service WHERE service LIKE %s;"""
add_service_query = """INSERT INTO order_service (order_id, service_id) VALUES (%s, %s);"""
add_treatment_query = """INSERT INTO order_treatment (order_id, medication) VALUES (%s, %s);"""

show_register_query = """
SELECT  orders.date, owners.last_name, owners.first_name, species.name, breeds.name, patient.date_of_birth, 
patient.nickname, vet_service.service, order_treatment.medication, orders.cost
FROM orders 
JOIN owners ON owners.id = orders.owner_id
JOIN patient ON patient.id = orders.patient_id
JOIN species ON species.id = patient.species_id
JOIN breeds ON breeds.id = patient.breed_id
LEFT JOIN order_service ON orders.id = order_service.order_id
JOIN vet_service ON vet_service.id = order_service.service_id
LEFT JOIN order_treatment ON orders.id = order_treatment.order_id  
ORDER BY orders.date DESC;     
"""

add_species_query = """INSERT INTO species (name) VALUES (%s);"""
get_species_id_query = """SELECT id FROM species WHERE name LIKE %s;"""
add_breed_query = """INSERT INTO breeds (species_id, name) VALUES (%s, %s);"""
get_breed_id_query = """SELECT id FROM breeds WHERE species_id = %s AND name LIKE %s;"""
get_breed_query = """SELECT name FROM breeds WHERE species_id = %s AND id = %s;"""
show_breeds_query = """SELECT id, name FROM breeds WHERE species_id = %s;"""
add_patient_query = """ INSERT INTO patients (species_id, breed_id, sex, date_of_birth, nickname, owner_id) 
VALUES (%s, %s, %s, %s, %s, %s);
"""





