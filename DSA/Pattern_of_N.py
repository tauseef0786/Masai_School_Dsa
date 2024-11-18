"""""
Description
• You are given a number stored in a variable with the name N
• You have to print all the numbers in the range from 1 to N*N, s
uch that there are exactly N numbers on each line
• For example, if the value stored in N = 3, then all the numbers i
n the range, from [1,9] need to be printed, such that there are 3
numbers on each line. Therefore, the required output is
1 2 3
4 5 6
7 8 9
Input
variable N
The first and the only line of the input contains the value stored in the
Output
Print all the numbers in the range from [1, N*NI, as shown in the probl
em statement, such that there are N numbers on each line
input:
4
output:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""""

def solve(N):
    count=1
    for i in range(N):
        for j in range(N):
            print(count,end=" ")
            count+=1
        print()    
          
N=4
solve(N)