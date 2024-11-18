"""""
Description
• You are given a number stored in a variable with the name num
• Check if the number is a prime number or not
• If the value stored in num, is a prime number print Yes, else prin
t No
Note : A prime number is a number, that is divisible by only
Input
The first and the only line of the input contains the value stored in num
Output
• If the value stored in num, is a prime number print Yes, else prin
t No
"""""


def solve(num):
    i=2
    count=0
    while i <= (num-1):
        if num%i==0:
            print("No")
            break
        i+=1
    else:
        print("Yes")
num=13
solve(num) # output 13



# second method 

def primeNumber(N):
    count=0
    for i in range(1,N+1):
        if N%i==0:
            count+=1      
    if count==2:
        print("Yes") 
    else:
        print("No")   
N=13        
primeNumber(N) #output No 