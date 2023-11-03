class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with a given size."""
        # The size of the hash table.
        self.size = size
        # The hash table.
        self.table = [None] * self.size
        # The number of key-value pairs stored in the hash table.
        self.count = 0

    def _hash(self, key):
        """Compute the initial hash value for a key."""
        # The hash value is computed as follows:
        return key % self.size

    def _rehash(self, old_hash, i):
        """Compute the new hash value using quadratic probing."""
        # The new hash value is computed as follows:
        return (old_hash + i**2) % self.size

    def put(self, key, value):
        """Store the key-value pair in the hash table."""
        # Compute the initial hash value.
        initial_hash = self._hash(key)
        # Initialize the hash value.
        hash_val = initial_hash
        # Initialize the counter.
        i = 1

        # Search for an empty slot or a slot with the same key.
        while self.table[hash_val] is not None and self.table[hash_val][0] != key:
            # If the key already exists, update the value.
            hash_val = self._rehash(initial_hash, i)
            # Increment the counter.
            i += 1
        # If the key does not exist, add the key-value pair.
        if self.table[hash_val] is None:
            # Increment the counter.
            self.count += 1
            # Add the key-value pair.
        self.table[hash_val] = (key, value)

    def get(self, key):
        """Retrieve the value associated with the given key."""
        # Compute the initial hash value.
        initial_hash = self._hash(key)
        # Initialize the hash value.
        hash_val = initial_hash
        # Initialize the counter.
        i = 1

        # Search for the key in the hash table.
        while self.table[hash_val] is not None:
            # Return the value if the key is found.
            if self.table[hash_val][0] == key:
                # Return the value.
                return self.table[hash_val][1]
            # Otherwise, rehash and search again.
            hash_val = self._rehash(initial_hash, i)
            # Increment the counter.
            i += 1

        # Return None if the key is not found.
        return None

    def __setitem__(self, key, value):
        """Support assignment using bracket notation."""
        # Add the key-value pair.
        self.put(key, value)

    def __getitem__(self, key):
        """Support retrieval using bracket notation."""
        # Retrieve the value.
        return self.get(key)

    def __contains__(self, key):
        """Support the 'in' keyword."""
        # Check if the key exists.
        return self.get(key) is not None


def test_hash_table():
    """Function to test the HashTable functionality."""
    # Initialize the hash table.
    hash_table = HashTable()
    # Add some key-value pairs.
    keys = [1, 2, 12, 22]
    # Note: The keys are chosen to demonstrate the quadratic probing.
    values = ["One", "Two", "Twelve", "Twenty Two"]
    # Add the key-value pairs.
    for key, value in zip(keys, values):
        # Add the key-value pair.
        hash_table[key] = value
    # Check if the key-value pairs were added correctly.
    for key, expected in zip(keys, values):
        # Retrieve the value.
        result = hash_table[key]
        # Check if the value is correct.
        assert (
            result == expected
        ), f"Expected {expected}, but got {result} for key {key}"


# Test the HashTable class.
if __name__ == "__main__":
    try:
        test_hash_table()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")

# Note for future improvement: I will be utilizing the `pytest` framework for more extensive testing and detailed error reports.
