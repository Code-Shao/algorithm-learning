import random

from 排序算法.cal_time import cal_time


def partition(li, left, right):
    tem = li[left]
    while left < right:
        while li[right] >= tem and left < right:
            right -= 1
        li[left] = li[right]
        while li[left] < tem and left < right:
            left += 1
        li[right] = li[left]
    li[left] = tem
    return left


# @cal_time
def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


# li = list(range(100000))
# random.shuffle(li)
# quick_sort(li, 0, len(li) - 1)
# # li = list(range(10))
# # random.shuffle(li)
li = [random.randint(0, 10) for i in range(10)]
print(li)
quick_sort(li, 0, len(li) - 1)
print(li)
