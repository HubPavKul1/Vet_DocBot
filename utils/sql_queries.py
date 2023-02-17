create_tables_query = """
CREATE TABLE IF NOT EXISTS users (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS owners (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS streets (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(250)
);

CREATE TABLE IF NOT EXISTS address (
    id BIGSERIAL PRIMARY KEY,
    owner_id INTEGER,
    street_id INTEGER,
    house VARCHAR(10),
    flat INTEGER,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE,
    FOREIGN KEY (street_id) REFERENCES streets(id) ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS species (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS breeds (
    id BIGSERIAL PRIMARY KEY,
    species_id INTEGER,
    name VARCHAR(50),
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS patients (
    id BIGSERIAL PRIMARY KEY,
    species_id INTEGER,
    breed_id INTEGER,
    sex VARCHAR(1),
    date_of_birth VARCHAR(20),
    nickname VARCHAR(50), 
    owner_id INTEGER,
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE,
    FOREIGN KEY (breed_id) REFERENCES breeds(id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS orders (
    id BIGSERIAL PRIMARY KEY,
    date VARCHAR(20),
    owner_id INTEGER,
    patient_id INTEGER,
    cost INTEGER,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS vet_service (
    id BIGSERIAL PRIMARY KEY,
    service VARCHAR(200),
    price INTEGER
);

CREATE TABLE IF NOT EXISTS order_service (
    id BIGSERIAL PRIMARY KEY,
    order_id INTEGER,
    service_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES vet_service(id) ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS order_service (
    id BIGSERIAL PRIMARY KEY,
    order_id INTEGER,
    medication TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
);
"""

user_exists_query = """SELECT user_id FROM users WHERE user_id = %s;"""
get_user_id_query = """SELECT id FROM users WHERE user_id = %s;"""
add_user_query = """INSERT INTO users (user_id, first_name, last_name) VALUES (%s, %s, %s);"""
get_streets_query = """SELECT id, name FROM streets WHERE name LIKE %s;"""
get_street_id = """SELECT id FROM streets WHERE name LIKE %s;"""
get_species_id_query = """SELECT id FROM species WHERE name LIKE %s;"""
get_breed_id_query = """SELECT id FROM breeds WHERE species_id = %s AND name LIKE %s;"""
get_service_id_query = """SELECT id FROM vet_service WHERE service LIKE %s;"""
show_users_query = """SELECT * FROM users ORDER BY id DESC;"""
add_owner_query = """INSERT INTO owners (first_name, last_name) VALUES (%s, %s);"""
show_streets_query = """SELECT * FROM streets;"""
add_address_query = """INSERT INTO address (owner_id, street_id, house, flat) VALUES (%s, %s, %s, %s);"""



