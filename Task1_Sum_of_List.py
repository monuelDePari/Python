from pip._vendor.msgpack.fallback import xrange


def Printer(some_list, sum_of_list, average):
    print(some_list, sum_of_list, average)


def generate_random():
    import random
    some_list = random.sample(xrange(100), 10)
    sum_of_list = sum(some_list)
    average = sum_of_list / len(some_list)
    Printer(some_list, sum_of_list, average)


def main():
    generate_random()


if __name__ == '__main__':
    main()
