from mocks import BOOKS, PAGES


class DummyDb:

    def __init__(self):
        self.__books_table = BOOKS
        self.__pages_table = PAGES

    def insert_book(self, book):
        self.__books_table.append(book)
        return book
        
    def retrieve_book(self, book_id):
        return self.__books_table[book_id]

    def list_books(self):
        return self.__books_table

    def retrieve_page(self, page_id):
        return self.__pages_table[page_id]