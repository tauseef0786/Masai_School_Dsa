def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

def EtoPowerX(x, n):
    if n == 1:
        return x + EtoPowerX(x, n - 1)
    if n == 0:
        return 1
    return (x ** n) / fact(n) + EtoPowerX(x, n - 1)

def runProgram(input):
    arr = list(map(int, input.strip().split()))
    x = arr[0]
    n = arr[1]
    print(f"{EtoPowerX(x, n):.4f}")

# Example usage
input = "4 2"  # Replace with your input
runProgram(input)
