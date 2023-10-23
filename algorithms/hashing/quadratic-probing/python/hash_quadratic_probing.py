class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [None] * self.size
        self.count = 0

    def _hash(self, key):
        """Compute the initial hash value for a key."""
        return key % self.size

    def _rehash(self, old_hash, i):
        """Compute the new hash value using quadratic probing."""
        return (old_hash + i**2) % self.size

    def put(self, key, value):
        """Store the key-value pair in the hash table."""
        initial_hash = self._hash(key)
        hash_val = initial_hash
        i = 1

        # Find an available slot or a slot with the same key to update.
        while self.table[hash_val] is not None and self.table[hash_val][0] != key:
            hash_val = self._rehash(initial_hash, i)
            i += 1

        if self.table[hash_val] is None:
            self.count += 1
        self.table[hash_val] = (key, value)

    def get(self, key):
        """Retrieve the value associated with the given key."""
        initial_hash = self._hash(key)
        hash_val = initial_hash
        i = 1

        # Search for the key in the hash table.
        while self.table[hash_val] is not None:
            if self.table[hash_val][0] == key:
                return self.table[hash_val][1]
            hash_val = self._rehash(initial_hash, i)
            i += 1

        # Return None if the key is not found.
        return None

    def __setitem__(self, key, value):
        """Support assignment using bracket notation."""
        self.put(key, value)

    def __getitem__(self, key):
        """Support retrieval using bracket notation."""
        return self.get(key)

    def __contains__(self, key):
        """Support the 'in' keyword."""
        return self.get(key) is not None


def test_hash_table():
    """Function to test the HashTable functionality."""
    hash_table = HashTable()

    # Sample data for testing.
    keys = [1, 2, 12, 22]
    values = ["One", "Two", "Twelve", "Twenty Two"]
    for key, value in zip(keys, values):
        hash_table[key] = value

    for key, expected in zip(keys, values):
        result = hash_table[key]
        assert (
            result == expected
        ), f"Expected {expected}, but got {result} for key {key}"


if __name__ == "__main__":
    try:
        test_hash_table()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")

# Note for future improvement: I will be utilizing the `pytest` framework for more extensive testing and detailed error reports.
