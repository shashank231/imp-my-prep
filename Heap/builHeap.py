
# 🔹 The Rule
# heapify(i) assumes:
# The left and right subtrees of i are already heaps.
# It just fixes the heap property at i by pushing the smaller value down.
# So if you start at the root before its children are fixed → you might bubble a small value into a subtree that is not yet a heap.
# That’s why we must fix from bottom to top:
# Make sure all small subtrees are heaps.
    # Then when you bubble down from a parent, it falls into an already-valid heap.
    # Result: whole tree is a heap.

# Function to "heapify" a subtree rooted at index i in array arr[]
# n = size of heap
def heapify(arr, n, i):
    largest = i               # Assume the parent is the largest
    left = 2 * i + 1          # Left child index
    right = 2 * i + 2         # Right child index

    # Step 1: Check if left child exists and is greater than parent
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Step 2: Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Step 3: If parent is NOT the largest, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]   # swap
        # After swap, the smaller element goes down to index `largest`
        # So we must heapify again at that position
        heapify(arr, n, largest)
9

# Function to build a max heap from an unsorted array
def buildHeap(arr):
    n = len(arr)
    # Step 1: Find index of last non-leaf node
    # (n//2 - 1) is the last node that has at least one child
    start = n // 2 - 1
    # Step 2: Heapify each node from bottom → top
    for i in range(start, -1, -1):
        heapify(arr, n, i)

# ---------------- DEMO ----------------
arr = [5, 12, 11, 13, 4, 6, 7]
print("Original array:", arr)
buildHeap(arr)
print("After building heap:", arr)
