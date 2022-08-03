from fun_test import fun_test


# @fun_test
def select_sort_simple(li):
    li_new = []
    print("hello")
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


@fun_test
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[min_loc], li[i] = li[i], li[min_loc]
