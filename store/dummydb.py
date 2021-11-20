from store.mocks import BOOKS


class DummyDb:

    def __init__(self):
        self.__db = BOOKS

    def insert_book(self, table, book):
        self.__db.append(book)
        return book
        
    def retrieve_book(self, table, book_id):
        return self.__db[book_id]

    def list_books(self, table):
        return self.__db

    def retrieve_page(self, table, book_id, page_id):
        return self.__db[book_id][page_id]