import random


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array that will have sorted numbers
    # Count array to store the count of occurrences of each digit
    count = [0] * 10

    # Store the count of occurrences of each digit in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr now contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead of passing the digit number, exp is passed.
    # exp is 10^i where i is the current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr


# Enter array length
length = int(input("Enter array length: "))

# Filling an array with random numbers
arr = [random.randint(1, 1000) for _ in range(length)]

print("Source array:", arr)

# Sort an array
sorted_arr = radix_sort(arr)
print("Sorted array:", sorted_arr)
