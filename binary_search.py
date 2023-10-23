def binary_search(arr, target):
    # Initialize two pointers: low at the beginning and high at the end of the array.
    low, high = 0, len(arr) - 1

    # Continue the loop as long as low doesn't surpass high.
    while low <= high:
        # Find the middle index of the current range.
        mid = (low + high) // 2
        
        # Check the element at the middle index.
        if arr[mid] == target:
            # Target found, return its index.
            return mid
        elif arr[mid] < target:
            # Target lies to the right of mid. Move the low pointer.
            low = mid + 1
        else:
            # Target lies to the left of mid. Move the high pointer.
            high = mid - 1

    # If the loop completes, the target was not found. Return -1.
    return -1

def test_binary_search():
    # List of test cases: each entry contains an array, a target, and the expected result.
    tests = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 4),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, -1),
        ([1, 3, 5, 7, 9], 3, 1),
        ([1, 3, 5, 7, 9], 2, -1)
    ]

    # Iterate through each test case.
    for arr, target, expected in tests:
        # Get the result from the binary_search function.
        result = binary_search(arr, target)
        # Assert that the result matches the expected outcome.
        assert result == expected, f"Expected {expected}, but got {result} for array {arr} and target {target}"

if __name__ == '__main__':
    try:
        # Run the tests.
        test_binary_search()
        print("All tests passed!")
    except AssertionError as e:
        # If any test fails, print a detailed error message.
        print(f"Test failed: {e}")

# Note for future improvement: I will be utilizing the `pytest` framework for more extensive testing and detailed error reports.
