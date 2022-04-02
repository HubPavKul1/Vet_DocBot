import psycopg2 as ps
from psycopg2 import Error
from data.config import DATABASE_URL


try:
    connection = ps.connect(DATABASE_URL, sslmode='require')
    cur = connection.cursor()
    print('Подключение к БД')
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cur.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")


