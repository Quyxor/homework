from random import choice
from string import digits, ascii_letters

values = list(digits + ascii_letters)

def password_generator(pass_len):
    while 1:
        yield ''.join([choice(values) for v in range(pass_len)])
