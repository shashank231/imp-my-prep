# ✅ What is a Min-Heap?
# A Min-Heap is a binary tree (usually complete) that satisfies the heap property:
# For every node, its value is ≤ the value of its children.
# That means the smallest element is always at the root.

# 📐 Structure
# A Min-Heap is typically represented as an array to save space and allow fast access:
# if heap root value at index 0
# For any element at index i:
# Left child: at index 2*i + 1
# Right child: at index 2*i + 2
# Parent: at index (i - 1) // 2

# ⚙️ Time Complexity of Min-Heap Operations
# Operation	     Description	                      Time Complexity
# insert(val)	 Add a new value and restore heap	    O(log n)
# extract_min()	 Remove and return min element (root)	O(log n)
# peek()	     Return min element (root)	            O(1)
# heapify()	     Build heap from unsorted array	        O(n)
# ✅ Most important: insert and extract_min take O(log n) time because the heap is a binary tree with height log n.

# ✅ “Use a heap when you're only interested in part of the sorted structure (like top-k), or when you need fast incremental min/max access.
# If you need the entire array sorted, just use sort() — it's equally efficient and simpler.”

import heapq

arr = [5, 3, 8, 1]
heapq.heapify(arr)             # Min-heap in-place
heapq.heappush(arr, 2)         # Insert 2

peek_min = arr[0]              # 🔍 Peek at the smallest element
print("Peek:", peek_min)       # Output: 1

min_elem = heapq.heappop(arr)  # Remove the smallest element
print("Popped:", min_elem)     # Output: 1
print("Heap Now:", arr)        # Output: [2, 3, 8, 5]

