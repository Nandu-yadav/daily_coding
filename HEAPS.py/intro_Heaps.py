class Heap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [-1]      # 1-based indexing
        self.size = 0

    # =========================
    # INSERT INTO MIN HEAP
    # =========================

    def insert(self, value):

        arr = self.arr
        size = self.size

        if size >= self.capacity:
            print("Heap Overflow")
            return

        arr.append(value)
        size += 1

        i = size

        while i > 1:

            parent = i // 2

            if arr[parent] > arr[i]:

                arr[parent], arr[i] = arr[i], arr[parent]

                i = parent

            else:
                break

        self.size = size

    # =========================
    # MIN HEAPIFY
    # =========================

    def min_heapify(self, i):

        arr = self.arr
        size = self.size

        while True:

            smallest = i

            left = 2 * i
            right = 2 * i + 1

            if left <= size and arr[left] < arr[smallest]:
                smallest = left

            if right <= size and arr[right] < arr[smallest]:
                smallest = right

            if smallest == i:
                break

            arr[i], arr[smallest] = arr[smallest], arr[i]

            i = smallest

    # =========================
    # EXTRACT MIN
    # =========================

    def extract_min(self):

        arr = self.arr
        size = self.size

        if size == 0:
            return None

        if size == 1:
            self.size -= 1
            return arr.pop()

        minimum = arr[1]

        arr[1] = arr[size]

        arr.pop()

        self.size -= 1

        self.min_heapify(1)

        return minimum

    # =========================
    # DELETE ROOT
    # =========================

    def delete_root(self):

        arr = self.arr
        size = self.size

        if size == 0:
            print("Nothing to delete")
            return

        arr[1] = arr[size]

        arr.pop()

        self.size -= 1

        self.min_heapify(1)

    # =========================
    # PRINT HEAP
    # =========================

    def print_heap(self):
        print(self.arr[1:])

    # =========================
    # MAX HEAPIFY
    # =========================

    @staticmethod
    def max_heapify(arr, n, i):

        while True:

            largest = i

            left = 2 * i
            right = 2 * i + 1

            if left <= n and arr[left] > arr[largest]:
                largest = left

            if right <= n and arr[right] > arr[largest]:
                largest = right

            if largest == i:
                break

            arr[i], arr[largest] = arr[largest], arr[i]

            i = largest

    # =========================
    # HEAP SORT
    # =========================

    @staticmethod
    def heap_sort(arr):

        n = len(arr) - 1

        # BUILD MAX HEAP
        for i in range(n // 2, 0, -1):
            Heap.max_heapify(arr, n, i)

        size = n

        while size > 1:

            arr[1], arr[size] = arr[size], arr[1]

            size -= 1

            Heap.max_heapify(arr, size, 1)

        return arr


# ==========================================
# DRIVER CODE
# ==========================================

heap = Heap(20)

heap.insert(50)
heap.insert(40)
heap.insert(30)
heap.insert(20)
heap.insert(10)

print("Min Heap:")
heap.print_heap()

print("\nExtract Min:")
print(heap.extract_min())

print("\nHeap After Extract:")
heap.print_heap()

print("\nDelete Root:")
heap.delete_root()

heap.print_heap()

# ==========================================
# HEAP SORT
# ==========================================

arr = [-1, 54, 53, 55, 52, 50]

print("\nOriginal Array:")
print(arr[1:])

sorted_arr = Heap.heap_sort(arr)

print("\nHeap Sorted Array:")
print(sorted_arr[1:])