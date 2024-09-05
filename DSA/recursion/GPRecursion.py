def raisTO(a, b):
    sum = 1
    for i in range(1, b + 1):
        sum = a ** i
    return sum

def GPRecu(n, r):
    if n == 0:
        return 1
    val = raisTO(r, n)
    ans = 1 / val + GPRecu(n - 1, r)
    return ans

def runProgram(input):
    n, r = map(int, input.strip().split())
    ans = GPRecu(n, r)
    print(f"{ans:.4f}")

# Example usage
input = "1 1"  # Replace with your input
runProgram(input)


