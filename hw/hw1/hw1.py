def odd(number):
    """Return whether the number is odd.

    >>> odd(2)
    False
    >>> odd(5)
    True
    """
    "*** YOUR CODE HERE ***"
    if number % 2 != 0:
        return True
    else:
        return False 

        
from math import sqrt

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two points (x1, y1) and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """
    "*** YOUR CODE HERE ***"
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def distance3d(x1, y1, z1, x2, y2, z2):
    """Calculates the 3D Euclidian distance between two points (x1, y1, z1) and
    (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976
    """
    "*** YOUR CODE HERE ***"
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-5, -1)
    -4
    """
    if b < 0:
        # If negative then substract it a - (-b)
        f = sub
    else:
        #If we positive just add it
        f = add 
    return f(a, b) # You can replace this line, but don't have to.

    
from math import sqrt


# All that is inside a parenthesis or square root can be done separately
# For this case we obtain first the inside sqrt because we use it for both cases + - 
def quadratic(a, b, c):
    """
    >>> quadratic(1, 0, -1)
    (-1.0, 1.0)
    >>> quadratic(1, 2, 1)
    (-1.0, -1.0)
    >>> quadratic(1, 3, -4)
    (-4.0, 1.0)
    """
    "*** YOUR CODE HERE ***"
    inside_sqrt = sqrt(b * b - 4 * a * c)
    return ((-b - inside_sqrt) / 2 * a , (-b + inside_sqrt) / 2 * a)
    
    
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    
# Remember that n and k are copies    
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    product = 1
    if k > n : k = n

    while(k):
        product *= n
        k -= 1
        n -= 1
    
    return product

# If we want ints remember to use //

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    steps = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else: 
            n = n * 3 + 1
        steps += 1
        print(n)
    return steps