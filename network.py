# Router
from routes import Mapper

# URLs
from api.books.urls import routes as book_urls


map = Mapper()

# Adds the URLs to the mapper instance
map.extend(book_urls)