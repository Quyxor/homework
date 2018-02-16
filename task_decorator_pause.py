import time


def pause(sleep_time):
    def decorator(function):
        def wrapper(*args, **kwargs):
            time.sleep(sleep_time)
            return function(*args, **kwargs)
        return wrapper
    return decorator
