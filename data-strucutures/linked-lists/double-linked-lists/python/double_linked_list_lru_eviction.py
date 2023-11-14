class Node:
    """
    Represents a node in the double linked list.

    Attributes:
        key (Any): The key stored in the node.
        value (Any): The value associated with the key.
        next (Node): The next node in the linked list.
        prev (Node): The previous node in the linked list.
    """

    def __init__(self, key, value):
        self.key = key  # Store the key in the node.
        self.value = value  # Store the value in the node.
        self.next = None  # Initially, there is no next node.
        self.prev = None  # Initially, there is no previous node.


class LRUCache:
    """
    A Least Recently Used (LRU) cache implemented using a double linked list and a hashmap.

    Attributes:
        capacity (int): The maximum capacity of the cache.
        hashmap (dict): A dictionary to store key-node pairs for O(1) access.
        head (Node): A dummy head node of the linked list to simplify operations.
        tail (Node): A dummy tail node of the linked list to simplify operations.
    """

    def __init__(self, capacity):
        self.capacity = capacity  # The maximum number of items the cache can hold.
        self.hashmap = {}  # Maps keys to their respective nodes in the linked list.
        # Initialize dummy head and tail nodes.
        self.head = Node(None, None)  # The head node does not store actual data.
        self.tail = Node(None, None)  # The tail node does not store actual data.
        self.head.next = self.tail  # Initially, the head points to the tail.
        self.tail.prev = self.head  # And the tail points to the head.

    def get(self, key):
        """
        Retrieves the value for the provided key in the cache.

        Parameters:
            key (Any): The key to retrieve the value for.

        Returns:
            Any: The value associated with the key, or -1 if the key is not in the cache.
        """
        if key in self.hashmap:
            # If the key is in the cache, move the corresponding node to the end (recently used).
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)
            return node.value  # Return the value of the node.
        return -1  # Key not found in the cache.

    def put(self, key, value):
        """
        Adds a key-value pair to the cache. If the key already exists, updates its value.
        Evicts the least recently used item if the cache is at capacity.

        Parameters:
            key (Any): The key to be added or updated.
            value (Any): The value associated with the key.
        """
        if key in self.hashmap:
            # If the key is already in the cache, remove its current node.
            self._remove(self.hashmap[key])

        node = Node(key, value)
        self._add(node)
        self.hashmap[key] = node  # Store the node in the hashmap.

        # Check if the capacity has been exceeded.
        if len(self.hashmap) > self.capacity:
            # Evict the least recently used item, which is next to the head.
            lru = self.head.next
            self._remove(lru)
            del self.hashmap[lru.key]  # Remove the evicted item from the hashmap.

    def _add(self, node):
        """
        Adds a node to the end of the linked list (just before the tail).

        Parameters:
            node (Node): The node to be added.
        """
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

    def _remove(self, node):
        """
        Removes a node from its current position in the linked list.

        Parameters:
            node (Node): The node to be removed.
        """
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
