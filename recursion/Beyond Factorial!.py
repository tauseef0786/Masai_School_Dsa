import math

def solve(n):
    def fact(n):
        if n == 2:
            return math.log(2)
        else:
            return math.log(n) + fact(n - 1)

    print(f"{fact(n):.4f}")

def run_program(input):
    n = int(input)
    solve(n)

# Example input
run_program(5)
