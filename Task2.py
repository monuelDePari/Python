def decorateHtml(function):
    def wrapper(string):
        func = function(string)

        make_replace = func.replace('&', '&amp').replace('"', '&quot').replace('<', '&lt').replace('>', '&gt')

        return make_replace

    return wrapper


@decorateHtml
def escape(string):
    return string


def main():
    string = input()
    print(escape(string))


if __name__ == '__main__':
    main()
