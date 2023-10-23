// Package main provides unit tests for the BinarySearch function.
package main

import (
	"testing" // Import the testing package from the standard library.
)

// TestBinarySearch is a test function for the BinarySearch function.
func TestBinarySearch(t *testing.T) {
	// Defining test cases for the BinarySearch function.
	// Each test case consists of an array, a target value, and the expected result.
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

		// Checking if the result matches the expected value.
		if result != test.expected {
			// Reporting a test failure using the Errorf method.
			t.Errorf("Test failed for array %v with target %d. Expected %d, got %d.", test.arr, test.target, test.expected, result)
		}
	}
}
