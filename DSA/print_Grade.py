"""""
Description
You are given a number, stored in the variable with the name total
If the following expression is true
total == 100, print "A", without quotes
Else if the following expression is true,
total > 90, print "B", without quotes
Else if the following expression is true,
total > 80, print "C", without quotes
Else, print "F", without quotes
Input
Input Format
First and only line of input contains a number which is total marks.
Constraints
N <= 100
Output
Output Format
Output the string
1.If marks equal to 100 print "A"
2.If marks greater than or equal to 90 print "B"
3.If marks greater than or equal to 80 print "C"
4.else print "F"
"""""

def solve(N):
    if N==100:
        print("A")
    elif N>=90:
        print("B")
    elif N>=80:
        print("C")
    else:
        print("F")
N=80    
solve(N)   