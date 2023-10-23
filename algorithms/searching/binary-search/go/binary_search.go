package main

import (
	"fmt"
)

// BinarySearch searches for the target in a sorted array and returns its index or -1 if not found.
func BinarySearch(arr []int, target int) int {
	low, high := 0, len(arr)-1

	for low <= high {
		mid := (low + high) / 2
		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1
}

func main() {
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
			fmt.Printf("Test failed for array %v with target %d. Expected %d, got %d.\n", test.arr, test.target, test.expected, result)
			return
		}
	}

	fmt.Println("All tests passed!")
}
