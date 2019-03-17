"""
Write a function that takes in a function cond and a number n and prints
numbers from 1 to n where calling cond on that number returns True.
"""
    
def keep_ints(cond,n):
    count,i = 0,1
    while i <= n:
        if cond(i):
            print(i)
        i += 1
    return count       

"""
Write a function similar to keep_ints like before, but now it takes in a
number n and returns a function that has one parameter cond. The returned
function prints out numbers from 1 to n where calling cond on that number
returns True.
"""

def keep_ints2(n):
    def counter(cond):
        count,i = 0,1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
        return count 
    return counter 

"""
Write a function that takes two numbers m and n and returns their product.
Assume m and n are positive integers. Use recursion, not mul or *!
"""        
def multiply(m,n):
    if n == 1:
        return m
    else:
        return multiply(m,n-1)+m

"""        
Write a recursive function that takes in an integer n and prints out a countdown from n to 1.
"""
def countdown(n):
    if n == 1:
        print(n)
    else:
        print(n)
        return countdown(n-1)
"""
How can we change countdown to count up instead without modifying a lot
of the code?
"""        
def countup(n):
    if n >= 1:
        countup(n-1)
        
"""
Write a recursive function that takes a number n and returns the sum of every
other digit, starting from the rightmost digit. Assume n is non-negative.
"""
def sum_every_other_digit(n):
    if n < 10:
        return n
    else:
        return sum_every_other_digit(n//100) + n%10

    
    

        
    
