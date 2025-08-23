class MaxHeap:
    def __init__(self):
        # Internal list to store heap elements
        self.heap = []

    # ---------------------------------------------------
    # Helper: Heapify a subtree rooted at index i
    # ---------------------------------------------------
    def heapify(self, n, i):
        largest = i               # Assume current index is largest
        left = 2 * i + 1          # Left child
        right = 2 * i + 2         # Right child

        # If left child exists and is larger than parent
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        # If right child exists and is larger than current largest
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        # If largest is not the parent, swap and continue heapifying
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            # Recursively heapify the affected subtree
            self.heapify(n, largest)

    # ---------------------------------------------------
    # Insert: Add a new value into the heap
    # ---------------------------------------------------
    def insert(self, value):
        # Step 1: Insert the new element at the end
        self.heap.append(value)
        i = len(self.heap) - 1   # index of new element

        # Step 2: Bubble up → fix heap property
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                # Swap if child is greater than parent
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent   # move up to parent index
            else:
                break

    # ---------------------------------------------------
    # Delete: Remove and return the root (max element)
    # ---------------------------------------------------
    def delete(self):
        n = len(self.heap)
        if n == 0:
            return None   # nothing to delete

        # Step 1: Swap root with the last element
        root = self.heap[0]
        self.heap[0] = self.heap[n - 1]
        self.heap.pop()  # remove last element

        # Step 2: Heapify from root to restore heap property
        self.heapify(len(self.heap), 0)

        return root  # return the deleted root


# ---------------- DEMO ----------------
if __name__ == "__main__":
    h = MaxHeap()

    # Insert elements
    h.insert(5)
    h.insert(12)
    h.insert(11)
    h.insert(13)
    h.insert(4)

    print("Heap array after inserts:", h.heap)

    # Delete root (max element)
    max_val = h.delete()
    print("Deleted max value:", max_val)
    print("Heap after deletion:", h.heap)
