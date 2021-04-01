height = int(input("Height: "))


def christmas(num) -> str:
    symbol = ""
    for i in range(1, num + 1):
        symbol += (num - i) * " " + (i * "* ")
        if num != i: symbol += "\n"
    return symbol


print(christmas(height))
