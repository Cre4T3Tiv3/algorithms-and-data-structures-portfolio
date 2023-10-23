---

# Binary Search in Go

This directory contains the Go implementation for the binary search algorithm.

## Overview

The binary search algorithm is a search algorithm that finds the position of a target value within a sorted array or list. It reduces the problem size by half with every iteration, resulting in a time complexity of \(O(\log n)\). 

## Implementation

### Function Signature

The main function `BinarySearch` is defined as:

```go
func BinarySearch(arr []int, target int) int
```

Where:
- `arr` is the sorted array in which we are searching for the target.
- `target` is the value we're looking for within the array.
- The function returns the index of the target in the array if found, or -1 if the target is not present.

## Testing

Go provides a robust built-in testing mechanism. The tests for the `BinarySearch` function are located in the `binary_search_test.go` file.

### Test Cases Structure

Test cases are structured in Go's idiomatic way of using slices of structs:

```go
tests := []struct {
	arr      []int
	target   int
	expected int
}
```

This provides a clean and descriptive way of defining multiple test cases.

### Running Tests

To run the tests, navigate to the directory containing the Go files and execute:

```bash
go test
```

If the tests pass, you'll see an output indicating the success, like:

```
PASS
ok  	binary_search	0.003s
```

In case of a test failure, Go will provide detailed information about which test cases failed and the reason behind the failure.

## Complexity Analysis

- **Time Complexity**: \(O(\log n)\) - As with each iteration, the list of possible elements gets halved.
  
- **Space Complexity**: \(O(1)\) - Constant space is used regardless of the input size.

## Additional Notes

If you're working outside of the GOPATH and encounter issues related to Go modules, you might need to initialize a new module by running `go mod init <module-name>` in your directory. If you're new to Go or working on simple projects, consider working inside your GOPATH (usually `~/go/src/`) or familiarizing yourself with Go modules, which are an essential part of Go's package management.

---