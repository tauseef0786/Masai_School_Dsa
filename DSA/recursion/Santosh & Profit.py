def time(N):
    if N == 0:
        return 1
    elif N < 0:
        return 0
    else:
        return time(N - 4) + time(N - 8)

def solve(N):
    print(time(N))

def runProgram(input):
    input = input.strip().split("\n")
    t = int(input[0])
    line = 1
    for _ in range(t):
        N = int(input[line])
        line += 1
        solve(N)

# Example usage
input = "3\n12\n8\n4"  # Replace with your input
runProgram(input)
