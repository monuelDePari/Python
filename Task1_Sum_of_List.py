class Sum_List:
    some_list = []
    sum = 0
    average = 0

    def generate_random(self, some_list=some_list, sum=sum, average=average):
        x = int(input())
        import random
        for t in range(x):
            some_list.append(random.randint(1, 100))
            sum += some_list[-1]
        average = sum / len(some_list)
        print(some_list, sum, average)


f = Sum_List()
f.generate_random()
