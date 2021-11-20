class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class BookIdIsRequired(Error):
    """ The 'book_id' field is required """
    pass

