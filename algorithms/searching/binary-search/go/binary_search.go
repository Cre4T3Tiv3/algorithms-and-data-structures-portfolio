// Package main provides a Go implementation of the binary search algorithm.
package main

import (
	"fmt" // Importing the fmt package for formatted I/O operations.
)

// BinarySearch searches for the target in a sorted array and returns its index or -1 if not found.
func BinarySearch(arr []int, target int) int {
	// Initializing low and high pointers at the start and end of the array respectively.
	low, high := 0, len(arr)-1

	// Continue the loop as long as the low pointer doesn't surpass the high pointer.
	for low <= high {
		// Compute the middle index.
		mid := (low + high) / 2

		// Check if the element at the middle index matches the target.
		if arr[mid] == target {
			return mid // If it matches, return the index.
		} else if arr[mid] < target {
			// If the element is less than the target, move the low pointer to the right.
			low = mid + 1
		} else {
			// If the element is greater than the target, move the high pointer to the left.
			high = mid - 1
		}
	}

	// If the loop completes without a match, return -1.
	return -1
}

// main function serves as the entry point of the application.
func main() {
	// Defining test cases. Each test case consists of an array, a target value, and the expected result.
	tests := []struct {
		arr      []int
		target   int
		expected int
	}{
		{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5, 4},
		{[]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 11, -1},
		{[]int{1, 3, 5, 7, 9}, 3, 1},
		{[]int{1, 3, 5, 7, 9}, 2, -1},
	}

	// Iterating through each test case.
	for _, test := range tests {
		// Calling the BinarySearch function and storing the result.
		result := BinarySearch(test.arr, test.target)

		// Comparing the result with the expected value.
		if result != test.expected {
			// Print an error message if the test fails.
			fmt.Printf("Test failed for array %v with target %d. Expected %d, got %d.\n", test.arr, test.target, test.expected, result)
			return // Exit the program if any test fails.
		}
	}

	// If all tests pass, print a success message.
	fmt.Println("All tests passed!")
}
