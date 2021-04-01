def print_function_name(function):
    def wrapper():
        function_name = function.__name__
        print("Executing: " + function_name)
        return function()

    return wrapper


@print_function_name
def print_ok():
    print("Ok")


print_ok()
