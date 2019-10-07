string = input()


def decoratorHtml(left, right):
    def decorator(function):
        def wrapper(n1):
            return left + function(n1) + right

        return wrapper

    return decorator


@decoratorHtml("<html>", "</html>")
def decorate(n):
    return n


print(decorate(string))
