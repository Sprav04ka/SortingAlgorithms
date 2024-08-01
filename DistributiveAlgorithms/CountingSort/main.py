import random


def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

    return arr


# Enter array length
length = int(input("Enter array length: "))

# Filling an array with random numbers
arr = [random.randint(1, 100) for _ in range(length)]

print("Source array:", arr)

# Sort an array
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
