# Task2
string = input()


def make_GT(function) -> str:
    def escapist():
        func = function()
        make_replace = func.replace('&', '&amp').replace('"', '&quot').replace('<', '&lt').replace('>', '&gt')
        return make_replace

    return escapist


@make_GT
def escape():
    return string


def main():
    print(escape())


if __name__ == '__main__':
    main()
