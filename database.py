# import psycopg2

from psycopg2 import pool

# def connection():
#     return psycopg2.connect(user='postgres',password='libertad26',database='atadb',host='localhost')


connection_pool = pool.SimpleConnectionPool(1, 10, 
                        database='atadb',
                        user='postgres',
                        password='Libertad26',
                        host='localhost'
                )