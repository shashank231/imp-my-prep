

import heapq

arr1 = [5, 3, 2, 1, 4]

heapq.heapify(arr1)

# arr1.append(6)
# arr1.append(-1)
# arr1.append(7)
# arr1.append(-2)


heapq.heappush(arr1, 6)
heapq.heappush(arr1, -1)
heapq.heappush(arr1, 7)
heapq.heappush(arr1, -2)

arr1.remove(1)

# heapq.heapify(arr1)

while arr1:
    a1 = heapq.heappop(arr1)
    print(a1)

