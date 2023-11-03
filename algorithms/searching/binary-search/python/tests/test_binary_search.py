from binary_search import binary_search


def test_binary_search():
    """
    A function to test the binary_search function.

    Raises:
    - AssertionError: If any of the tests fail.
    """

    # List of test cases: each entry contains an array, a target, and the expected result.
    tests = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 4),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, -1),
        ([1, 3, 5, 7, 9], 3, 1),
        ([1, 3, 5, 7, 9], 2, -1),
    ]

    # Iterate through each test case.
    for arr, target, expected in tests:
        # Get the result from the binary_search function.
        result = binary_search(arr, target)
        # Assert that the result matches the expected outcome.
        assert (
            result == expected
        ), f"Expected {expected}, but got {result} for array {arr} and target {target}"

# Test the binary_search function.
if __name__ == "__main__":
    try:
        # Run the tests.
        test_binary_search()
        # Print a success message if all tests pass.
        print("All tests passed!")
    except AssertionError as e:
        # If any test fails, print a detailed error message.
        print(f"Test failed: {e}")
