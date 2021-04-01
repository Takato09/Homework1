def _range(start: int, stop=None, step=1) -> iter:
    if stop is None:
        stop = start
        start = 0

    i = 1
    while start < stop:
        yield start
        i += 1
        start += step


print(list(range(1, 12, 2)))
