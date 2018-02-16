from collections import namedtuple


def return_namedtuple(*decor_args):
    def decorator(function):
        def wrapper(*args, **kwargs):
            func_result = function(*args, **kwargs)
            if isinstance(func_result, tuple):
                record = namedtuple("MyNamedTuple", list(decor_args))
                named_tuple = record(*func_result)
                return named_tuple
            else:
                return func_result
        return wrapper
    return decorator
