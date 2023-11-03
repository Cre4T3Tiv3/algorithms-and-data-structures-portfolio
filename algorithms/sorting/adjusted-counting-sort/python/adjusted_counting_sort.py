def adjusted_counting_sort(arr):
    """
    Function to sort an array using the adjusted counting sort method.
    Parameters:
        arr (list[int]): List of integers to be sorted.

    Returns:
        list[int]: List of integers in sorted order.
    """
    # Initialize the frequency array.
    freq = [0] * 100

    # Count the frequencies of each element.
    for num in arr:
        # Increment the frequency of the current element.
        freq[num] += 1

    # Initialize the sorted array.
    sorted_arr = []
    # Iterate through the frequency array.
    for index, count in enumerate(freq):
        # Add the current element to the sorted array.
        sorted_arr.extend([index] * count)

    # Return the sorted array.
    return sorted_arr


# Test the adjusted_counting_sort function.
if __name__ == "__main__":
    # Get the number of elements.
    n = int(input("Enter the number of elements: ").strip())
    # Get the elements.
    arr = list(
        map(int, input("Enter the elements separated by spaces: ").rstrip().split())
    )
    # Sort the array.
    result = adjusted_counting_sort(arr)
    # Print the sorted array.
    print("Sorted Array:", " ".join(map(str, result)))
