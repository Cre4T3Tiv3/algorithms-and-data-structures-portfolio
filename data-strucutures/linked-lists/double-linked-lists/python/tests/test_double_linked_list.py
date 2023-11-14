import unittest
from double_linked_list import DoubleLinkedList


class TestDoubleLinkedList(unittest.TestCase):
    """
    A test suite for the DoubleLinkedList class.

    Methods:
        test_append_and_display(): Tests appending nodes and displaying the list.
        test_is_empty(): Tests checking if the list is empty.
        test_size(): Tests calculating the size of the list.
    """

    def test_append_and_display(self):
        """
        Test appending elements to the list and displaying them.
        """
        dll = DoubleLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        self.assertEqual(
            dll.display(), [1, 2, 3]
        )  # Check if the list displays correctly.

    def test_is_empty(self):
        """
        Test if the is_empty method correctly identifies an empty list.
        """
        dll = DoubleLinkedList()
        self.assertTrue(dll.is_empty())  # Initially, the list should be empty.
        dll.append(1)
        self.assertFalse(
            dll.is_empty()
        )  # After appending, the list should not be empty.

    def test_size(self):
        """
        Test if the size method correctly returns the number of elements in the list.
        """
        dll = DoubleLinkedList()
        self.assertEqual(dll.size(), 0)  # Initially, the size should be 0.
        dll.append(1)
        dll.append(2)
        self.assertEqual(
            dll.size(), 2
        )  # After appending two elements, the size should be 2.


if __name__ == "__main__":
    unittest.main()
