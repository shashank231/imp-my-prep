import heapq


# kth smallest element
def kth_largest(arr, k):
    # Step 1: Build a min-heap of first k elements
    min_heap = arr[:k]
    heapq.heapify(min_heap)   # O(k)

    # Step 2: Process remaining elements
    for x in arr[k:]:
        # If current element is bigger than heap's min (root)
        if x > min_heap[0]:
            heapq.heappop(min_heap)     # Remove smallest among current k
            heapq.heappush(min_heap, x) # Insert new larger element

    # Step 3: Root of heap is the k-th largest
    return min_heap[0]

# ---------------- DEMO ----------------
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}-th largest element is:", kth_largest(arr, k))


