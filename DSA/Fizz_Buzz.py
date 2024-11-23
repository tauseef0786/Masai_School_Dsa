
"""""
Fizzz buzzz

Description
• You are given a number stored in a variable with the name num
• For all numbers in the range [1, num], including num
1. If the number is divisible by 3 and 5 both, print FizzBuzz
2. Else If the number is divisible by 3, print "Fizz", withou
3. Else If the number is divisible by 5, print "Buzz"
, withou
4. Else, print the number as it is
Input
The first line contains T, the number of test cases.
The first line of each test case contains the value stored in the variable
num
Output
Print the required output, according to the conditions shown in the pr
oblem statement
Sample Input 
2
1
3
Sample Output

1
1
2
Fizz

"""

def fizz_buzz(num):
   for i in range(1,num+1):
      if i%3==0 and i%5==0:
         print("FizzBuzz")
      elif i%3==0 and i%5!=0:
         print("Fizz")
      elif i%3!=0 and i%5==0: 
         print("Buzz")
      else:
         print(i)
         
fizz_buzz(1)         
fizz_buzz(3)         