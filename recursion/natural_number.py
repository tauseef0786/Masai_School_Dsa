def fun(n):
    if n==1:
        return 1
    else:
        return n+fun(n-1)
n=5
result=fun(n)
print(result)   



""""
Definition: - The process in which a function calls it-self, directly or indirectly is called recursion

natural number of n 
n=5
natural_num=1+2+3+4+5=15
-----------------dry run------------

result-->calling--->fun(n)                              now parent(f(n)) caaling to child 

fun(n)=fun(5) ---> != 1 false ------>  return 5+fun(4)     10+5=15
fun(5)=fun(4) ---> != 1 false ------>  return 4+fun(3)     6+4=10
fun(4)=fun(3) ---> != 1 false ------>  return 3+fun(2)     3+3=6
fun(3)=fun(2) ---> != 1 false ------>  return 2+fun(1)     1+2=3  
fun(2)=fun(1) ---> != 1 true  ------>  return 1              



6+


"""
