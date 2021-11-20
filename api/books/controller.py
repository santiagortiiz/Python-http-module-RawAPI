# Standard libraries
import json

# Databases
from store import (
    Postgres as pg, 
    Redis as redis,
)

# Errors
from utils.errors import BookIdIsRequired

default_store = pg
default_cache = redis

TABLE = 'books'

class Book:

    def __init__(self, injected_store=default_store, injected_cache=default_cache):
        self.__store = injected_store()
        self.__cache = injected_cache()

    def insert_book(self, table=TABLE, book=None, **kwargs):
        try:            
            return self.__store.insert_book(table, book)
        except Exception as e:
            return str(e)

    def list_books(self, table=TABLE, **kwargs):
        try:
            return self.__store.list_books(table)
        except Exception as e:
            return str(e)

    def retrieve_book(self, table=TABLE, **kwargs):
        try:
            book_id = int(kwargs.get('book_id', None))
            return self.__store.retrieve_book(table, book_id)
            
        except Exception as e:
            return str(e)

    def retrieve_page(self, table=TABLE, book=None, page=None, **kwargs):
        try:
            return self.__store.retrieve_page(table, book, page)
        except Exception as e:
            return str(e)