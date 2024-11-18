"""""
Description
You are given a number, stored in a variable with the name num
Find the sum of all even numbers greater than zero, and less than or e
qual to the value stored in num
For example, if the value stored in num = 5, then all the even number
s smaller than or equal to 5, and greater than zero are
2
4
Therefore, the sum becomes, sum = 2 + 4 = 6, which is the require
d output
Input
ariable num
The first and the only line of input contains the number stored in the v
Output
Print the sum of all even numbers greater than zero, and less than or e
qual to the value stored in num
"""""

def solve(num):
  if num%2 != 0:
      num = num - 1
  s1 = 0
  for i in range(2,num+1,2):
       s1 = s1 + i
  print(s1)

num=6
solve(num)  # output 12