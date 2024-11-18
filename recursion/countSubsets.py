def countSubsets(arr, n, sum):
    if sum == 0:
        return 1
    if n == 0 and sum != 0:
        return 0
    
    if arr[n - 1] > sum:
        return countSubsets(arr, n - 1, sum)
    
    return countSubsets(arr, n - 1, sum) + countSubsets(arr, n - 1, sum - arr[n - 1])

# Direct input
input_data = "4 10\n1 2 3 4"

# Process the input
lines = input_data.strip().split("\n")
N, X = map(int, lines[0].split())
array = list(map(int, lines[1].split()))

# Calculate and print the result
result = countSubsets(array, N, X)
print(result)
