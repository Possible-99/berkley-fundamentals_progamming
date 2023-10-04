"""
# >>> from operator import add, mul
# >>> mul(add(5, 6), 8)
# 88
# >>> print('x')
# x
# >>> y = print('x')
# x
# >>> print(y)
# None
# >>> print(add(4, 2), print('a'))
# a 
# 6 None
# >>> def foo(x):
#         print(x)
#         return x + 1
# >>> def bar(y, x):
#         print(x - y)
# >>> foo(3)
# 3
# 4
# >>> bar(3)

# >>> bar(6, 1)
# -5
# >>> bar(foo(10), 11)
# 10
# 1
"""

# A prime is a number that only can by divided by itsels and 1
# 1 , 2, 3, 4, 5 , 6, 7, 8, 9, 10
# We can try to divide the number by each one of the numbers until n
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1: return False
    
    for num in range(2, n):
        if n % num == 0:
            return False
    
    return True


