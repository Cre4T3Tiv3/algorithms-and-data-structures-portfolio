import unittest
from double_linked_list_lru_eviction import LRUCache


class TestLRUCache(unittest.TestCase):
    """
    Test suite for the LRUCache class.

    This class contains multiple unit tests to ensure the proper functionality of the LRUCache.
    It tests key aspects like cache insertion, retrieval, capacity management, and value updating.
    """

    def setUp(self):
        """
        Set up method to initialize the LRUCache instance before each test.

        This method is called before each individual test method, and it sets up the LRUCache with a capacity of 2.
        """
        self.cache = LRUCache(2)  # Initialize LRUCache with a capacity of 2.

    def test_put_and_get(self):
        """
        Test the put and get methods of LRUCache.

        This test ensures that values can be put into the cache and retrieved correctly.
        It also tests the basic eviction policy where the least recently used item is removed when the cache is full.
        """
        # Adding key-value pairs to the cache.
        self.cache.put(1, 1)
        self.cache.put(2, 2)

        # Retrieving value for key 1, which should be present.
        self.assertEqual(self.cache.get(1), 1)

        # Adding another key-value pair which should trigger eviction of key 2.
        self.cache.put(3, 3)

        # Trying to retrieve value for key 2, which should have been evicted.
        self.assertEqual(self.cache.get(2), -1)

    def test_capacity(self):
        """
        Test the eviction policy when the cache exceeds its capacity.

        This test checks if the cache correctly evicts the least recently used item when a new item is added beyond its capacity.
        """
        # Filling the cache to its capacity.
        self.cache.put(1, 1)
        self.cache.put(2, 2)

        # Adding another item to trigger eviction of the least recently used item.
        self.cache.put(3, 3)

        # Checking if the least recently used item (key 1) has been evicted.
        self.assertEqual(self.cache.get(1), -1)
        # Checking if the newly added item is present.
        self.assertEqual(self.cache.get(3), 3)

    def test_update_value(self):
        """
        Test updating the value of an existing key in the cache.

        This test ensures that if a key already exists in the cache, its value can be updated, and the updated value is retrieved correctly.
        """
        # Adding a key-value pair to the cache.
        self.cache.put(1, 1)

        # Updating the value of the existing key.
        self.cache.put(1, 10)

        # Checking if the value of the key is updated.
        self.assertEqual(self.cache.get(1), 10)


if __name__ == "__main__":
    unittest.main()
