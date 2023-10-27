# Adjusted Counting Sort Algorithm

## Introduction

The Adjusted Counting Sort is a non-comparison based sorting algorithm that determines the frequency of each distinct element in the list and sorts them based on these frequencies. This directory contains a Python implementation of the Adjusted Counting Sort algorithm and its corresponding tests.

## Table of Contents

- [Introduction](#introduction)
- [Algorithm Description](#algorithm-description)
- [Complexity Analysis](#complexity-analysis)
- [Usage](#usage)
- [Testing](#testing)
- [Future Improvements](#future-improvements)

## Algorithm Description

The Adjusted Counting Sort algorithm works by creating a frequency array of fixed size (100 in our case). For every element in the input list, the algorithm increments the corresponding index in the frequency array. The sorted list is then constructed by reading the frequency array.

## Complexity Analysis

- **Time Complexity**: O(n + k) - Where `n` is the size of the input list and `k` is the range of the input. In our case, k is constant (100), making the time complexity linear.
- **Space Complexity**: O(k) - Space is used for the frequency array. Again, k is constant (100), so space complexity is O(1).

## Usage

To use the Adjusted Counting Sort function, simply import it and call it with a list of integers:

```python
from algorithms.sorting.adjusted_counting_sort.python.adjusted_counting_sort import adjusted_counting_sort

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = adjusted_counting_sort(arr)
print(sorted_arr)
```

## Testing

The code comes with unit tests. To run the tests, navigate to the directory containing `test_adjusted_counting_sort.py` and execute the script:

```
python test_adjusted_counting_sort.py
```

If all tests pass, you will see an "OK" message. Otherwise, a detailed error message will be displayed.

## Future Improvements

Plans are underway to enhance the algorithm to handle a broader range of numbers and to provide detailed error reports. Contributions and suggestions are welcome!
