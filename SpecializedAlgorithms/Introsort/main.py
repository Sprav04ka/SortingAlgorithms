import random
import math


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def introsort_util(arr, begin, end, maxdepth):
    size = end - begin
    if size < 16:
        insertion_sort(arr, begin, end)
    elif maxdepth == 0:
        heap_sort(arr[begin:end + 1])
    else:
        pivot = partition(arr, begin, end)
        introsort_util(arr, begin, pivot - 1, maxdepth - 1)
        introsort_util(arr, pivot + 1, end, maxdepth - 1)


def introsort(arr):
    maxdepth = int(math.log2(len(arr))) * 2
    introsort_util(arr, 0, len(arr) - 1, maxdepth)
    return arr


# Enter array length
length = int(input("Enter array length: "))

# Filling an array with random numbers
arr = [random.randint(1, 100) for _ in range(length)]

print("Source array:", arr)

# Sort an array
sorted_arr = introsort(arr)
print("Sorted array:", sorted_arr)
