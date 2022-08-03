import random


def fun_test(fun):
    def wrapper(*args, **kwargs):
        li = [random.randint(10, 20) for i in range(10)]
        print(li)
        fun(li)
        print(li)

    return wrapper()
