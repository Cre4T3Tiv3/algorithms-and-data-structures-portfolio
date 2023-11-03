def binary_search(arr, target):
    """
    A function to implement the binary search algorithm.

    Parameters:
    - arr: A sorted list of items.
    - target: The item to search for in the list.

    Returns:
    - int: The index of the target if found, otherwise -1.
    """
    # Initialize the low and high pointers.
    low, high = 0, len(arr) - 1

    # Loop until the low and high pointers meet.
    while low <= high:
        # while low < high:
        mid = (low + high) // 2

        # Check if the target is at the middle.
        if arr[mid] == target:
            # Target found. Return the index.
            return mid
        elif arr[mid] < target:
            # Target lies to the right of mid. Move the low pointer.
            low = mid + 1
        else:
            # Target lies to the left of mid. Move the high pointer.
            high = mid - 1

    # Target not found. Return -1.
    return -1

# Driver code.
if __name__ == "__main__":
    # Get the input from the user.
    arr = [
        int(x)
        for x in input("Enter a sorted list of numbers separated by spaces: ").split()
    ]
    # Get the target from the user.
    target = int(input("Enter the number you want to search for: "))
    # Call the binary search function.
    result = binary_search(arr, target)
    # Print the result.
    if result != -1:
        print(f"Element {target} is present at index {result}.")
    else:
        print(f"Element {target} is not present in the array.")
