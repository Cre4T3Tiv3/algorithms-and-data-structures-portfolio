class HashTable:
    """
    A simple hash table implementation using chaining for collision handling.

    Attributes:
        size (int): The number of buckets in the hash table.
        table (list): The hash table, with each bucket being a list to handle collisions.
    """

    def __init__(self):
        # Initialize hash table with a fixed size and empty buckets.
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        """
        Computes the hash value for a given key.

        Parameters:
            key (int): The key for which to compute the hash.

        Returns:
            int: The hash value, determining the bucket where the key-value pair will be stored.
        """
        return key % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.

        If the key already exists, its value is updated. Otherwise, the pair is added to the table.

        Parameters:
            key (int): The key to insert into the hash table.
            value (Any): The value associated with the key.
        """
        hash_key = self.hash_function(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, _ = kv
            if key == k:
                bucket[i] = (key, value)  # Update existing key-value pair.
                return
        bucket.append((key, value))  # Add new key-value pair.

    def remove(self, key):
        """
        Removes a key-value pair from the hash table.

        Parameters:
            key (int): The key to be removed.
        """
        hash_key = self.hash_function(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, _ = kv
            if key == k:
                del bucket[i]  # Remove the key-value pair.
                break

    def lookup(self, key):
        """
        Retrieves the value associated with a given key.

        Parameters:
            key (int): The key for which to retrieve the value.

        Returns:
            Any: The value associated with the key, or None if the key is not found.
        """
        hash_key = self.hash_function(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if key == k:
                return v  # Return the value if key is found.
        return None  # Return None if key is not found.

    def print_table(self):
        """
        Prints the contents of the hash table for debugging purposes.
        """
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}:", bucket)
