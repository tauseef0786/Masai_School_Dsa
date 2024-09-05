def NumberOfWays(N):
    if N == 0:
        return 1
    if N < 0:
        return 0
    return NumberOfWays(N - 1) + NumberOfWays(N - 2) + NumberOfWays(N - 3)

def solve(N):
    print(NumberOfWays(N))

def runProgram(input):
    N = int(input)
    solve(N)

# Example usage
input = "5"  # Replace with your input
runProgram(input)
