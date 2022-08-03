import heapq
import random

li = [random.randint(10, 20) for i in range(10)]
print(li)
heapq.heapify(li)
print(li)

for i in range(len(li)):
    print(heapq.heappop(li))
