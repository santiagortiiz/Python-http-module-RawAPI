# Standard libraries
import os
from dotenv import load_dotenv
load_dotenv()


# PostgreSQL
import psycopg2 as pg


class Postgres:
    
    def __init__(self):
        self.__cnx = pg.connect(
            host = os.environ.get('PG_HOST'),
            port = os.environ.get('PORT'),
            user = os.environ.get('PG_USER'),
            password = os.environ.get('PG_PASSWORD'),
            dbname = os.environ.get('PG_DB_NAME'),
        )

        self.__cursor = self.__cnx.cursor()

    def insert_book(self, table, book):
        return self.__store.insert_book(table, book)

    def retrieve_book(self, table, book_id):
        sql = f'SELECT * FROM {table} WHERE id={book_id}'
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def list_books(self, table):
        sql = f'SELECT * FROM {table}'
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()

    def retrieve_page(self, table, book_id, page):
        sql = f'''
            SELECT content
            FROM {table}
            WHERE 
                book_id = {book_id} 
                AND page = {page}
            '''
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()