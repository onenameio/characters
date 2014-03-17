from .charset import charset_to_int, int_to_charset

# https://en.bitcoin.it/wiki/Base58Check_encoding
B58_CHARS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def b58_to_int(s):
    return charset_to_int(s, B58_CHARS)

def int_to_b58(val):
    return int_to_charset(val, B58_CHARS)

def is_b58(s):
    for char in s:
        if char not in B58_CHARS:
            return False
    return True
