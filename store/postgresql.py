# Standard libraries
import os

# PostgreSQL
import psycopg2 as pg

# Mocks
from store.mocks import BOOKS


class Postgres:
    
    def __init__(self):
        self.__cnx = pg.connect(
            user='postgres', 
            password='r00t', 
            host='localhost',
            dbname='testdb',
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

    def retrieve_page(self, table, book, page):
        return self.__store.retrieve_page(table, book, page)