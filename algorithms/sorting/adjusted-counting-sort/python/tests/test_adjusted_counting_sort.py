import sys

sys.path.append(
    "../../.."
)  # To include the parent directories in the module search path

from algorithms.sorting.adjusted_counting_sort.python.adjusted_counting_sort import (
    adjusted_counting_sort,
)
import unittest


class TestAdjustedCountingSort(unittest.TestCase):
    """
    Unit tests for the Adjusted Counting Sort Algorithm
    """

    def test_basic(self):
        """
        Basic tests for the Adjusted Counting Sort
        """
        arr = [4, 2, 2, 8, 3, 3, 1]
        self.assertEqual(adjusted_counting_sort(arr), [1, 2, 2, 3, 3, 4, 8])

        arr = [9, 7, 5, 3, 1]
        self.assertEqual(adjusted_counting_sort(arr), [1, 3, 5, 7, 9])

    def test_empty(self):
        """
        Test for an empty list
        """
        arr = []
        self.assertEqual(adjusted_counting_sort(arr), [])

    def test_single_element(self):
        """
        Test for a list with a single element
        """
        arr = [5]
        self.assertEqual(adjusted_counting_sort(arr), [5])


if __name__ == "__main__":
    unittest.main()
