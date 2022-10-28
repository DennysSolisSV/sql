import psycopg2

def connection():
    return psycopg2.connect(user='postgres',password='libertad26',database='atadb',host='localhost')