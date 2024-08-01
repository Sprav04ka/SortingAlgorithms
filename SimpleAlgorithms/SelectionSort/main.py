import random


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = arr[i]
        p = i
        for j in range(i+1, n):
            if min > arr[j]:
                min = arr[j]
                p = j
        if p != i:
            arr[i], arr[p] = arr[p], arr[i]
    return arr


# Enter array length
length = int(input("Enter array length: "))

# Filling an array with random numbers
arr = [random.randint(1, 100) for _ in range(length)]
9
print("Source array:", arr)

# Sort an array
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
