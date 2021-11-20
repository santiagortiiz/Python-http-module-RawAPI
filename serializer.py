# Utilities
from utils.decorators import (
    dict_to_bytes, 
    list_to_bytes,
    str_to_bytes,
)


@str_to_bytes
@list_to_bytes
@dict_to_bytes
def to_bytes(data):
    return data
    
