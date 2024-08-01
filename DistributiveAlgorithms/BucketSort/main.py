import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucket_sort(arr):
    max_val = max(arr)
    size = max_val // len(arr) + 1
    buckets = [[] for _ in range(size)]

    for i in range(len(arr)):
        j = arr[i] // size
        buckets[j].append(arr[i])

    for i in range(len(buckets)):
        insertion_sort(buckets[i])

    result = []
    for i in range(len(buckets)):
        result.extend(buckets[i])

    return result


# Enter array length
length = int(input("Enter array length: "))

# Filling an array with random numbers
arr = [random.randint(1, 100) for _ in range(length)]

print("Source array:", arr)

# Sort an array
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
