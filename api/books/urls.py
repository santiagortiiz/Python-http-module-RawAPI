# Routes
from routes.route import Route

# Controllers
from .index import book


routes = [
    Route(
        None, 
        "/books", 
        controller=book.insert_book, 
        action="insert"
    ),
    Route(
        "library", 
        "/books", 
        controller=book.list_books, 
        action="list"
    ),
    Route(
        None, 
        "/books/{book_id}", 
        controller=book.retrieve_book, 
        action="retrieve"
    ),
    Route(
        "Books", 
        "/books/{book_id}/{page_id}/{format_id}", 
        controller=book.retrieve_page, 
        action="read"
    ),
]
