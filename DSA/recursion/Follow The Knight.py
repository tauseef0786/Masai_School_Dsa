def solve(r, c, N):
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def follow_the_knight(arr, N, R, C):
        if R < 0 or R > 9 or C < 0 or C > 9:
            return
        elif N == 0:
            arr[R][C] = 1
            return
        else:
            follow_the_knight(arr, N - 1, R - 2, C + 1)
            follow_the_knight(arr, N - 1, R - 2, C - 1)
            follow_the_knight(arr, N - 1, R + 2, C + 1)
            follow_the_knight(arr, N - 1, R + 2, C - 1)
            follow_the_knight(arr, N - 1, R - 1, C - 2)
            follow_the_knight(arr, N - 1, R - 1, C + 2)
            follow_the_knight(arr, N - 1, R + 1, C - 2)
            follow_the_knight(arr, N - 1, R + 1, C + 2)

    follow_the_knight(board, N, r, c)
    
    count = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                count += 1

    print(count)

def run_program(input_str):
    input_list = list(map(int, input_str.strip().split()))
    i = input_list[0] - 1
    j = input_list[1] - 1
    N = input_list[2]
    solve(i, j, N)

# Example input
example_input = "4 10 1"
run_program(example_input)
