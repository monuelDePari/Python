# Task2
string = input()


def make_GT(function) -> str:
    def escapist():
        func = function()
        make_replace = func.replace('>', '&gt')
        return make_replace
    return escapist


def make_IT(function) -> str:
    def escapist():
        func = function()
        make_replace = func.replace('<', '&lt')
        return make_replace
    return escapist


def make_Amp(function) -> str:
    def escapist():
        func = function()
        make_replace = func.replace('&', '&amp')
        return make_replace
    return escapist


def make_Quot(function) -> str:
    def escapist():
        func = function()
        make_replace = func.replace('"', '&quot')
        return make_replace
    return escapist


@make_Quot
@make_GT
@make_IT
@make_Amp
def escape():
    return string


print(escape())
