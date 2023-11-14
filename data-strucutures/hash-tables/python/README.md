# Simple Hash Table Implementation in Python

## Overview

This Python module implements a basic hash table using chaining to handle collisions. The hash table is designed for an e-commerce platform's product inventory, mapping product IDs (integers) to product information (dictionaries).

## Features

- Insert product information into the hash table.
- Lookup product information by product IDs.
- Remove product information from the hash table.
- Print the contents of the hash table.

## Usage

To use this hash table, create an instance of `HashTable` and use its methods to perform various operations like insertion, lookup, and removal of product information.

Example:

```python
from hash_table_simple import HashTable

# Creating a hash table instance
hash_table = HashTable()

# Inserting product information
hash_table.insert(1001, {"product_name": "Wireless Mouse", "price": 29.99})
hash_table.insert(1002, {"product_name": "Keyboard", "price": 19.99})

# Looking up a product
print(hash_table.lookup(1001))  # Outputs: {'product_name': 'Wireless Mouse', 'price': 29.99}

# Updating a product's price
hash_table.insert(1001, {"product_name": "Wireless Mouse", "price": 24.99})

# Removing a product
hash_table.remove(1002)

# Printing the hash table contents
hash_table.print_table()
```
