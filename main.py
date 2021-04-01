import string
import secrets


class Phone:
    number = ''.join(secrets.choice(string.digits) for i in range(11))

    def __init__(self, brand, os):
        self.brand = brand
        self.os = os


class Samsung(Phone):

    def __init__(self, brand, os):
        super().__init__(brand, os)
        self.brand = "Samsung"


class Apple(Phone):

    def __init__(self, brand, os):
        super().__init__(brand, os)


Samsung = Phone("Samsung", "android")
print(Samsung.brand, Samsung.os, Samsung.number)
Apple = Phone("Apple", "ios")
print(Apple.brand, Apple.os, Apple.number)

