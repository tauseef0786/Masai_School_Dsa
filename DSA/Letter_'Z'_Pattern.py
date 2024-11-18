"""""

Description
Write a Java program to print the letter 'Z' pattern using nested loops.
The pattern should have a specified number of rows, and the letter 'Z'
should be formed using asterisks (*) as shown in the sample input.
Input
A single integer 'N' where (3 ≤ N ≤ 1000) representing the number of r
ows in the 'Z' pattern.
Output
The 'Z' pattern consisting of asterisks.
sample input:
5

output:
*****
   *
  *
 *
*****

"""""

def solve(N):
    for i in range(N):
        for j in range(N):
            if i==0 or i==N-1 or i+j==N-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
N=5
solve(N) 