import string
import secrets


class Phone:
    os = None
    brand = None

    def __init__(self):
        self.number = ''.join(secrets.choice(string.digits) for i in range(11))


class Samsung(Phone):
    def __init__(self,os):
    self.os = "android"



class Apple(Phone):
    os = "IOS"
    brand = "Apple"


print(Samsung.brand, Samsung.os, Phone.number)
print(Apple.brand, Apple.os, Phone.number)
