package main

import (
	"testing"
)

func TestBinarySearch(t *testing.T) {
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

	for _, test := range tests {
		result := BinarySearch(test.arr, test.target)
		if result != test.expected {
			t.Errorf("Test failed for array %v with target %d. Expected %d, got %d.", test.arr, test.target, test.expected, result)
		}
	}
}
