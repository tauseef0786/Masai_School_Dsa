""""

The factorial of a positive integer N is the product of all positive
integers less than or equal to n:
Given a number N your task is to write a program that calculates
factorial of N

"""
def factorial(N):
    if N == 0 or N == 1:  
        return 1
    else:
        return N * factorial(N - 1)

N = int(input())    
print(factorial(N))
