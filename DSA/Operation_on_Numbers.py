"""""

Description
• You are given a number, stored in a variable with the name numb
er . Perform the following operations on the value stored in the
number
1. Multiply the value by 3
2. Add 7 after it
3. Subtract 10 from it
After performing all the above operations, print the updated value
Input
The first and the only line of the input contains the number, stored in t
he variable number
Constraints
1 <= N <= 30
Output
Print a single integer, denoting the updated value of the number store
d, after performing all the operations, given in the problem statement
sample input:
4

Output:
9
"""""

def perform_operations(number):
   print(number*3+7-10)

n=4
perform_operations(n)   
