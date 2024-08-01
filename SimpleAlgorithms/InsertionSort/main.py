import random


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr


# Enter array length
length = int(input("Enter array length: "))

# Filling an array with random numbers
arr = [random.randint(1, 100) for _ in range(length)]

print("Source array:", arr)

# Sort an array
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
