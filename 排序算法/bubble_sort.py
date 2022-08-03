import random

from 排序算法.cal_time import cal_time


@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return


li = list(range(10000))
random.shuffle(li)
bubble_sort(li)
