def sum(n):
    """Using recursion, computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    "*** YOUR CODE HERE ***"
    if n < 2 : 
        return 1
    else:
        return sum(n - 1) + n
    
    
def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k % 10 == 7:
        return True
    if k == 0: 
        return False
    
    return has_seven(k // 10)
    
    
def filter(f, seq):
    """Filter a sequence to only contain values allowed by filter.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> def divisible_by5(x):
    ...     return x % 5 == 0
    >>> filter(is_even, [1,2,3,4])
    [2, 4]
    >>> filter(divisible_by5, [1, 4, 9, 16, 25, 100])
    [25, 100]
    """
    "*** YOUR CODE HERE ***"
    if seq == []:
        return []
    
    ls = []
    if f(seq[0]):
        ls.append(seq[0])
    
    return ls + filter(f , seq[1 : ]) 


def decimal(n):
    """Return a list representing the decimal representation of a number.

    >>> decimal(55055)
    [5, 5, 0, 5, 5]
    >>> decimal(-136)
    ['-', 1, 3, 6]
    """
    "*** YOUR CODE HERE ***"

    if n  < 0 : 
        return  ['-']+ decimal(-n)
    
    if n < 10:
        return [n]
    
    
    return decimal(n // 10) + [n % 10]
    
    
""" 
    65055
    
    func acumul + res part -> We do a reverse so we build the number in the correct order
    stack = [5, 5 , 0, 5, 6]
    We add to the end!!!!
    We get the reverse order provided by the stack 
    [6] + [5] = [6,5]
    [6,5] + [0] = [6,5,0]
    [6,5,0] + [5]  = [6,5,0,5]
    [6,5,0 ,5] + [5]  = [6,5,0,5,5]

    res part + func acuml -> We are going to have the number reversed    
    We insert at the beginning!!!!
    We get the stack!!!!
    stack = [5, 5 , 0, 5, 6]
    [5] + [6] = [5, 6]
    [0] + [5 , 6]  = [0, 5 , 6]
    [5] + [0,5 , 6]  = [5, 0, 5 , 6]
    [5] + [5,0,5 , 6]  = [5,5, 0, 5 , 6]
"""


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    
    It doesn make a difference if we start from the end and by doing this we don't need a grid or another
    assignment to start in the beginning

    We start from 0 ,0  and n - 1, m - 1
    So we stop when we reach n  = 1  and m  = 1 for compensating that we doesn't decrement m and m
    We can divide the problem in two parts:
    1. Go down
    2. Go left
    
    For each one we have a recursive function which generates a recursion tree where at each level we can take both
    decisions. If we are able to reach (1, 1) then we return 1.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    
    if n < 1 or m  < 1:
        return 0
    
    if n == 1 and m == 1:
        return 1
    
    return paths(m - 1 , n) + paths(m, n - 1)