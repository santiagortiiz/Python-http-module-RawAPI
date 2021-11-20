# Controller
from .controller import Book

# Database
from store import Postgres, DummyDb


# store = DummyDb
store = Postgres
book = Book(store)