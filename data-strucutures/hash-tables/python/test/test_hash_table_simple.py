import unittest
from hash_table_simple import HashTable


class TestHashTable(unittest.TestCase):
    """
    A test suite for the HashTable class.

    This class contains various unit tests to ensure the correct functionality of the HashTable,
    particularly focusing on insertion, removal, update, and lookup operations.
    """

    def setUp(self):
        """
        Set up method to create a new HashTable instance before each test.

        This method is called before every test, ensuring that each test is run with a fresh HashTable.
        """
        self.hash_table = HashTable()

    def test_insert_and_lookup(self):
        """
        Test the insertion of a key-value pair and its subsequent lookup.

        This test checks if a key-value pair can be successfully inserted into the hash table and
        then correctly retrieved using the lookup method.
        """
        product_info = {"product_name": "Wireless Mouse", "price": 29.99}
        self.hash_table.insert(1001, product_info)
        self.assertEqual(self.hash_table.lookup(1001), product_info)

    def test_remove(self):
        """
        Test the removal of a key from the HashTable.

        This test inserts a key-value pair and then removes it, ensuring that the key
        no longer exists in the hash table.
        """
        product_info = {"product_name": "Wireless Mouse", "price": 29.99}
        self.hash_table.insert(1001, product_info)
        self.hash_table.remove(1001)
        self.assertIsNone(self.hash_table.lookup(1001))

    def test_update_value(self):
        """
        Test updating the value of an existing key in the HashTable.

        This test checks if the value associated with a key can be updated and if the updated value
        is correctly retrieved through a lookup.
        """
        initial_product_info = {"product_name": "Wireless Mouse", "price": 29.99}
        updated_product_info = {"product_name": "Wireless Mouse", "price": 24.99}
        self.hash_table.insert(1001, initial_product_info)
        self.hash_table.insert(1001, updated_product_info)
        self.assertEqual(self.hash_table.lookup(1001), updated_product_info)


if __name__ == "__main__":
    unittest.main()
