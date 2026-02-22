import numpy as np
import time
import sys
sys.setrecursionlimit(100000)

#*****MERGESORT
def mergeSort (arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    sortedLeft = mergeSort (leftHalf)
    sortedRight = mergeSort (rightHalf)
    return merge (sortedLeft, sortedRight)

def merge (left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right) :
        if left[i] < right[j]:
            result.append (left[i])
            i+=1
        else:
            result.append (right[j])
            j+=1
    result.extend (left[i:])
    result.extend (right[j:])
    return result

#****HEAPSORT
def heapify(arr, n, i):
    largest = i    
    l = 2 * i + 1    
    r = 2 * i + 2  
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

#****QUICKSORT
def quickSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        arr[mid], arr[high] = arr[high], arr[mid]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

#***GEN DATA
N = 1000000
max_Val = 1000000

datasets = [("1 (Nguyên, Tăng dần)", np.sort(np.random.randint(-max_Val, max_Val, N)).tolist()),
            ("2 (Nguyên, Giảm dần)", np.sort(np.random.randint(-max_Val, max_Val, N))[::-1].tolist()),
            ("3 (Nguyên, Ngẫu nhiên)", np.random.randint(-max_Val, max_Val, N).tolist()),
            ("4 (Nguyên, Ngẫu nhiên)", np.random.randint(-max_Val, max_Val, N).tolist()),
            ("5 (Nguyên, Ngẫu nhiên)", np.random.randint(-max_Val, max_Val, N).tolist()),

            ("6 (Thực, Ngẫu nhiên)", np.random.uniform(-max_Val, max_Val, N).tolist()),
            ("7 (Thực, Ngẫu nhiên)", np.random.uniform(-max_Val, max_Val, N).tolist()),
            ("8 (Thực, Ngẫu nhiên)", np.random.uniform(-max_Val, max_Val, N).tolist()),
            ("9 (Thực, Ngẫu nhiên)", np.random.uniform(-max_Val, max_Val, N).tolist()),
            ("10 (Thực, Ngẫu nhiên)", np.random.uniform(-max_Val, max_Val, N).tolist()) ]

print(f"{'Dãy dữ liệu':<25} | {'QuickSort':<10} | {'HeapSort':<10} | {'MergeSort':<10} | {'Numpy Sort':<10}")
print("-" * 80)


for label, data in datasets:
    # 1. QuickSort
    arr = data.copy()
    start = time.time()
    quickSort(arr, 0, len(arr) - 1)
    time_quick = (time.time() - start) * 1000

    # 2. HeapSort
    arr = data.copy()
    start = time.time()
    heapSort(arr)
    time_heap = (time.time() - start) * 1000

    # 3. MergeSort
    arr = data.copy()
    start = time.time()
    mergeSort(arr)
    time_merge = (time.time() - start) * 1000

    # 4. Numpy Sort
    arr_np = np.array(data)
    start = time.time()
    np.sort(arr_np)
    time_np = (time.time() - start) * 1000

    print(f"{label:<25} | {time_quick:10.2f} | {time_heap:10.2f} | {time_merge:10.2f} | {time_np:10.2f}")

