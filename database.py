# import psycopg2

from psycopg2 import pool

# def connection():
#     return psycopg2.connect(user='postgres',password='libertad26',database='atadb',host='localhost')

class Database:
        connection_pool = None

        def initialise(self):
                Database.connection_pool = pool.SimpleConnectionPool(1, 10, 
                        database='atadb',
                        user='postgres',
                        password='libertad26',
                        host='localhost'
                )

class CursorFromConnectionFromPool:
        def __init__(self):
                self.connection = None
                self.cursor = None

        def __enter__(self):
                self.connection = connection_pool.getconn()
                self.cursor = self.connection.cursor()
                return self.cursor

        def __exit__(self, exception_type, exception_value, exception_traceback):
                if exception_value is not None:
                        self.connection.rollback()
                else:
                        self.cursor.close()
                        self.connection.commit()
                        connection_pool.putconn(self.connection)