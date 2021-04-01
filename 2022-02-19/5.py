import math

start = int(input("Start: "))
end = int(input("End: "))


def is_prime(i):
    m = min(i, int(math.sqrt(end)))
    l = range(2, m)
    r = map(lambda x: i % x == 0, l)
    return not any(r)


ls = range(start, end)
_list = list(filter(is_prime, ls))

for x in _list: print(x)
