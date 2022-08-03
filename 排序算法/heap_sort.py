import copy
import random

from 排序算法.print_tree import print_tree


def sift(li, low, high):
    tmp = li[low]
    i = 2 * low + 1
    while i <= high:
        j = 2 * low + 2
        if j <= high and li[i] > li[j]:
            i = j
        if li[i] < li[low]:
            li[i], li[low] = li[low], li[i]
            low = i
        else:
            break
        i = 2 * low + 1


def heap_sort(li):
    n = len(li)
    for i in range((n - 1 - 1) // 2, -1, -1):
        sift(li, i, len(li) - 1)
    for i in range(len(li) - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)


li = list(range(20))
li = [random.randint(0, 10) for i in range(10)]
random.shuffle(li)
# li = [5, 10, 1, 9, 6]
print_tree(li)
heap_sort(li)
print_tree(li)
