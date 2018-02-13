from collections import namedtuple


def return_namedtuple(*args):

    def decorator(function):
        func_result = function()

        if isinstance(func_result, tuple):
            record = namedtuple("MyNamedTuple", list(args))
            return lambda: record(*func_result)

    return decorator
