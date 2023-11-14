# Python Double Linked List and LRU Cache Implementation

## Overview

This directory includes two Python modules: one implementing a basic double linked list and the other a Least Recently Used (LRU) cache using a double linked list. These implementations showcase fundamental data structure concepts in Python.

---

### Double Linked List (Module: `double_linked_list.py`)

#### Description

The Double Linked List module provides a basic implementation of a doubly linked list, allowing for efficient insertion and deletion of elements from both ends of the list.

#### Features

- Append data to the end of the list.
- Display the contents of the list.
- Check if the list is empty.
- Get the size of the list.

#### Usage

```python
from double_linked_list import DoubleLinkedList

dll = DoubleLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print(dll.display())  # Output: [1, 2, 3]
```

### LRU Cache (Module: `double_linked_list_lru_eviction.py`)

#### Description

The LRU Cache module implements a Least Recently Used (LRU) cache mechanism. It evicts the least recently accessed items first and provides O(1) time complexity for both get and put operations.

#### Features

- Get the value of a key from the cache.
- Add a key-value pair to the cache.
- Automatically evict the least recently used item when the cache exceeds its capacity.

#### Usage

```python
from double_linked_list_lru_eviction import LRUCache

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)  # Evicts key 2
print(cache.get(2))  # Output: -1 (not found)
print(cache.get(3))  # Output: 3
```
