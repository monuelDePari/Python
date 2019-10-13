string = input()
html_tag = input()


def decoratorHtml(tag):
    def decorator(function):
        def wrapper(n1):
            return "<" + tag + ">" + function(n1) + "<" + tag + "/>"

        return wrapper

    return decorator


@decoratorHtml(html_tag)
def decorate(n):
    return n


def main():
    print(decorate(string))


if __name__ == '__main__':
    main()
