def fibonacci(stop_count):
    x, y = 0, 1

    for n in range(stop_count):
        x, y = y, x + y
        yield x
