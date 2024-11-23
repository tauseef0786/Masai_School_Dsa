"""""
Easy Wood Cutter
Description
You are given a number, stored in a variable with the name N . Check i
i the the number is divisible by 3 or not
If its possible, print "Yes"
Else print "No"
Hint : A number can be divided into 3 parts, if the numbe
r is completely divisible by 3, that is, the answer of th
e operation number % 3 is zero
Input
Input Format :
First line contains length of wood : N
Constraints :
N < 1000
Output
Print Yes/No based on the length
Sample Input 
6
Sample Output
Yes

"""

def check_divisibility_by_3(N):
    if N%3 == 0:
        print("Yes")
    else:
        print("No")

check_divisibility_by_3(6)        
