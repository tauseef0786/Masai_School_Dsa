def superdigit(string):
    if len(string) == 1:
        return int(string)
    else:
        sum = 0
        for char in string:
            sum += int(char)
        return superdigit(str(sum))

def solve(string, k):
    initial_superdigit = superdigit(string)
    combined_sum = str(initial_superdigit * k)
    print(superdigit(combined_sum))

def runProgram(input):
    input = input.strip().split(" ")
    string = input[0]
    k = int(input[1])
    solve(string, k)

# Example usage
input = "123 3"  # Replace with your input
runProgram(input)
