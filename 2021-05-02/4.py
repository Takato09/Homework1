from functools import wraps


def call_counter(function):
    counter = {}

    @wraps(function)
    def wrapper():
        counter[function] = counter.get(function, 0) + 1
        print(f"Function {function.__name__} has been called {counter[function]} times")
        result = function()
        return result

    return wrapper


@call_counter
def print_ok():
    print("Ok")


@call_counter
def print_hi():
    print("Hi")


print_ok()
print_ok()
print_hi()
print_ok()
