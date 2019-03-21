# -*- coding: utf-8 -*-
"""
In discussion 1, we implemented the function is prime, which takes in a
positive integer and returns whether or not that integer is prime, iteratively.
Now, let’s implement it recursively! As a reminder, an integer is considered
prime if it has exactly two unique factors: 1 and itself.
"""
def is_prime(n):
    def prime_helper(x):
        if x >= n:
            return True
        elif n%x == 0:
            return False
        else:
            return prime_helper(x+1)
    return prime_helper(2)

"""
Define a function make fn repeater which takes in a one-argument function
f and an integer x. It should return another function which takes in one
argument, another integer. This function returns the result of applying f to
x this number of times.
Make sure to use recursion in your solution.
"""        
def make_func_repeater(f,x):
    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return f(repeat(n-1))
    return repeat 
    
incr_1 = make_func_repeater(lambda x: x+1,1)

"""
I want to go up a flight of stairs that has n steps. I can either take 1 or 2
steps each time. How many different ways can I go up this flight of stairs?
Write a function count_stair_ways that solves this problem for me. Assume
n is positive.  
"""   
        
def count_stair_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

"""
Consider a special version of the count_stairways problem, where instead
of taking 1 or 2 steps, we are able to take up to and including k steps at
a time.
Write a function count_k that figures out the number of paths for this scenario. Assume n and k are positive.
"""


def count_k(n,k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif k == 0:
        return 0
    else:
        return count_k(n-k,k) + count_k(n,k-1)

"""
Here’s a part of the Pascal’s triangle:
Column: 0 1 2 3 4 ...
Row 0: 1
Row 1: 1 1
Row 2: 1 2 1
Row 3: 1 3 3 1
Row 4: 1 4 6 4 1
...
Every number in Pascal’s triangle is defined as the sum of the item above
it and the item that is directly to the upper left of it, use 0 if the entry is
empty. Define the procedure pascal(row, column) which takes a row and a
column, and finds the value at that position in the triangle.
"""        
                                                
def pascal(row,column):
    if row == 0 and column == 0:
        return 1
    if row == 0 and column > 0:
        return 0
    if column == 0:
        return 1
    else:
        return pascal(row-1,column-1) + pascal(row-1,column)
