"""
Module for the Adjusted Counting Sort Algorithm
"""


def adjusted_counting_sort(arr):
    """
    Function to sort an array using the adjusted counting sort method.
    Parameters:
        arr (list[int]): List of integers to be sorted.

    Returns:
        list[int]: List of integers in sorted order.
    """
    # Create a frequency array of size 100 initialized with zeros
    freq = [0] * 100

    # Populate the frequency array based on input elements
    for num in arr:
        freq[num] += 1

    # Return the sorted array based on frequencies
    sorted_arr = []
    for index, count in enumerate(freq):
        sorted_arr.extend([index] * count)

    return sorted_arr


if __name__ == "__main__":
    n = int(input("Enter the number of elements: ").strip())
    arr = list(
        map(int, input("Enter the elements separated by spaces: ").rstrip().split())
    )
    result = adjusted_counting_sort(arr)
    print("Sorted Array:", " ".join(map(str, result)))
