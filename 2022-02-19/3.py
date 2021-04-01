number = int(input("Enter number:"))


def multiplier(num):
    for coefficient in range(1, 11):
        result = coefficient*num
        yield result


print(*multiplier(number), sep='\n')
