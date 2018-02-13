import time


def pause(sek):

    def decorator(function):
        time.sleep(sek)
        function()

    return decorator
