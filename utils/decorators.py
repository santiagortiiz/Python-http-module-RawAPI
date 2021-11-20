''' Converters for the required data structures '''
# Standard libraries
import json
from datetime import date

# Constants
ENCODING = 'utf-8'


def str_to_bytes(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if type(data) == str:
            data = data.encode(ENCODING)
        return data
    return wrapper

def list_to_bytes(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if type(data) == list:
            data = json.dumps(data).encode(ENCODING)
        return data
    return wrapper

def dict_to_bytes(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if type(data) == dict:
            data = json.dumps(data).encode(ENCODING)
        return data
    return wrapper