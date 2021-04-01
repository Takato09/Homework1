def MyRange(stop=None, start=None, step=None, skip=3) -> iter:
    if stop is None:
        stop = start
        start = 0

    i = 1
    while start < stop:
        if i == skip:
            i = 1
        else:
            yield start
            i += 1
        start += step


for x in MyRange(stop=10, start=1, step=-2):
    print(x)