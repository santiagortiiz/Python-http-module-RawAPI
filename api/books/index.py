''' 
Select database and controller to use.
    Database drivers working:
    + Postgres
    + DummyDb
'''
# Controller
from .controller import Book

# Database
from store import Postgres, DummyDb


store = DummyDb
# store = Postgres
book = Book(store)