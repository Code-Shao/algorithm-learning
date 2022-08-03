from cal_time import cal_time


@cal_time
def linear_search(li, val):
    for index, v in enumerate(li, 0):
        if v == val:
            return index
    return None


@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] < val:
            left += 1
        else:
            right -= 1
    else:
        return None


n = 100000
li = list(range(n))
linear_search(li, n // 2)
binary_search(li, n // 2)
