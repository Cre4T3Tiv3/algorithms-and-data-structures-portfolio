---

# Binary Search Algorithm

## Introduction

The binary search is an efficient algorithm for finding an item from a sorted list of items. This repository contains a Python implementation of the binary search algorithm and its corresponding tests.

## Table of Contents

1. [Introduction](#introduction)
2. [Algorithm Description](#algorithm-description)
3. [Complexity Analysis](#complexity-analysis)
4. [Usage](#usage)
5. [Testing](#testing)
6. [Future Improvements](#future-improvements)

## Algorithm Description

The binary search works by dividing a sorted list into halves and determining which half of the list the desired item is likely to be in. It then repeats this process, halving the list further until the item is found or it's concluded that the item isn't in the list.

## Complexity Analysis

- **Time Complexity**: `O(log n)` - With each iteration, the list of possible elements is halved, making the time complexity logarithmic.
  
- **Space Complexity**: `O(1)` - Constant space is used regardless of the input size.

## Usage

To use the binary search function, simply import it and call it with a sorted list and a target item:

```python
from binary_search import binary_search

arr = [1, 2, 3, 4, 5]
target = 3
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")
```

## Testing

The code comes with a basic testing function. To run the tests, execute the `binary_search.py` script:

```bash
python binary_search.py
```

If all tests pass, you will see an "All tests passed!" message. Otherwise, a detailed error message will be displayed.

## Future Improvements

Plans are underway to incorporate the `pytest` framework for more extensive testing and to provide detailed error reports. Contributions and suggestions are welcome!

---