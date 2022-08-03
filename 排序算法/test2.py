import copy

li = list(range(10))
li2 = copy.deepcopy(li)
li2[1] = 10000
print(li, li2)
