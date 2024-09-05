def way7(k, arr, N):
    if k == 0:
        return 1
    elif k < 0:
        return 0
    else:
        t = 0
        for i in range(N):
            t += way7(k - arr[i], arr, N)
        return t

def solve(K, N, arr):
    print(way7(K, arr, N))

def runProgram():
    import sys
    input = sys.stdin.read().strip().split("\n")
    in1 = list(map(int, input[0].split()))
    K = in1[0]
    N = in1[1]
    arr = list(map(int, input[1].split()))
    solve(K, N, arr)

# For testing purpose, we can define a sample input manually
input_data = "3 3\n1 2 3"
import sys
from io import StringIO

sys.stdin = StringIO(input_data)
runProgram()

