import random


def timsort(arr):
    return sorted(arr)


# Enter array length
length = int(input("Enter array length: "))

# Filling an array with random numbers
arr = [random.randint(1, 100) for _ in range(length)]

print("Source array:", arr)

# Sort an array
sorted_arr = timsort(arr)
print("Sorted array:", sorted_arr)
