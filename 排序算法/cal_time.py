import time


def cal_time(func):
    def wrapper2(*args, **kwargs):
        t1 = time.time()
        print(t1)
        result = func(*args, **kwargs)
        t2 = time.time()
        print(t2)
        print("%s函数运行了%e   secs" % (func.__name__, t2 - t1))
        return result

    return wrapper2
