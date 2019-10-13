import hashlib
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapped


@my_decorator
def function_to_wrap(string):
    hashedString = hashlib.sha1(string.encode())
    return hashedString


if __name__ == "__main__":
    print(function_to_wrap('Hello World'))
