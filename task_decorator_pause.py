import time


def pause(sleep_time):

    def decorator(function):
        time.sleep(sleep_time)
        return function

    return decorator
