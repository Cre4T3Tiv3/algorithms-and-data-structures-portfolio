import sys

sys.path.append(
    "../../.."
)  # To include the parent directories in the module search path

# Import the function to test.
from adjusted_counting_sort import adjusted_counting_sort

import unittest


# The parent class.
class TestAdjustedCountingSort(unittest.TestCase):
    """
    Unit tests for the Adjusted Counting Sort Algorithm
    """

    def test_basic(self):
        """
        Basic tests for the Adjusted Counting Sort
        """
        # Test 1: Test for a list with no duplicates.
        arr = [4, 2, 2, 8, 3, 3, 1]
        # The expected output.
        self.assertEqual(adjusted_counting_sort(arr), [1, 2, 2, 3, 3, 4, 8])

        # Test 2: Test for a list with duplicates.
        arr = [9, 7, 5, 3, 1]
        # The expected output.
        self.assertEqual(adjusted_counting_sort(arr), [1, 3, 5, 7, 9])

    def test_empty(self):
        """
        Test for an empty list
        """
        # Test 1: Test for an empty list.
        arr = []
        # The expected output.
        self.assertEqual(adjusted_counting_sort(arr), [])

    def test_single_element(self):
        """
        Test for a list with a single element
        """
        # Test 1: Test for a list with a single element.
        arr = [5]
        # The expected output.
        self.assertEqual(adjusted_counting_sort(arr), [5])


# Run the unit tests.
if __name__ == "__main__":
    unittest.main()
