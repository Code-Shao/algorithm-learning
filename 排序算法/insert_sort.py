import random


def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        tem = li[i]
        while j >= 0 and li[j] > tem:
            li[j], li[j + 1] = li[j + 1], li[j]
            j = j - 1
        li[j + 1] = tem


li = [random.randint(1, 9) for i in range(0, 9)]
print(li)
insert_sort(li)
print(li)
