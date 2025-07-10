import heapq
from collections import Counter


def top_k_frequent_elements(arr, k):
    # Step 1: Count frequencies
    freq_map = Counter(arr)
    
    # Step 2: Use a min-heap of size k
    min_heap = []
    for key, freq in freq_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, key))  # Tuple compares from left to right so automatically takes first value as key for mantaining heap property
        else:
            # Compare with smallest in heap
            if freq > min_heap[0][0]:
                heapq.heappop(min_heap)                   # Remove smallest
                heapq.heappush(min_heap, (freq, key))     # Push current

    # Step 3: Sort results by frequency descending
    # Extract top-k elements
    # Since it's a min-heap, this will be in ascending order.
    # Reverse if needed.
    result = sorted(min_heap, reverse=True)
    print("Top", k, "frequent elements:")
    for freq, key in result:
        print(f"Element: {key}, Frequency: {freq}")


def connectRopes(arr):
    heapq.heapify(arr)
    minSum = 0

    while (len(arr) > 2):
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        print(a, b)
        minSum += (a+b)
        heapq.heappush(arr, (a+b))
    
    print(minSum + sum(arr))
    

ar1 = [4, 3, 2, 6]
connectRopes(ar1)
