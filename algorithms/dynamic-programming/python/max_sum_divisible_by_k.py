def max_weight_divisible_by_K(arr, K):
    """
    A function to find the maximum weight of apples divisible by K.

    Parameters:
    - arr: A list of weights of apples.
    - K: An integer to divide the sum of weights of apples by.

    Returns:
    - int: The maximum weight of apples divisible by K.
    """
    # Initialize the dp table.
    n = len(arr)

    # Initialize the dp table.
    dp = [[-float("inf")] * K for _ in range(n + 1)]
    # Base case.
    dp[0][0] = 0

    # Loop over the apples.
    for i in range(1, n + 1):
        # Loop over the remainders.
        for j in range(K):
            # Check if the current apple is not included.
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            # Check if the current apple is included.
            dp[i][(j + arr[i - 1]) % K] = max(
                dp[i][(j + arr[i - 1]) % K], dp[i - 1][j] + arr[i - 1]
            )
    # Return the maximum weight of apples divisible by K.
    return max(0, dp[n][0])

# Driver code.
if __name__ == "__main__":
    # Initialize the array of weights of apples.
    arr = [43, 1, 17, 26, 15]
    # Initialize the value of K.
    K = 16
    # Call the max_weight_divisible_by_K function.
    result = max_weight_divisible_by_K(arr, K)
    # Print the result.
    print(f"Maximum weight of apples divisible by {K} is: {result}")
