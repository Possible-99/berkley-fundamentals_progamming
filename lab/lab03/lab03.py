def square(x):
    return x * x

def halve(x):
    return x // 2

def twice(f,x):
    """Apply f to the result of applying f to x
    >>> twice(square,3)
    81
    >>> twice(square,4)
    256
    >>> twice(halve, 32)
    8
    >>> twice(halve, 80)
    20
    """
    "*** YOUR CODE HERE ***"
    return f(f(x))



def increment(x):
    return x + 1

def decrement(x):
    return x - 1

def double(x):
    return x * 2

def apply_n(f, x, n):
    """Apply function f to x n times.

    >>> apply_n(increment, 2, 10)
    12
    >>> apply_n(decrement, 5, 8)
    -3
    >>> apply_n(double, 7, 3)
    56
    """
    "*** YOUR CODE HERE ***"
    for i in range(n):
        x = f(x)
    return x


def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    "*** YOUR CODE HERE ***"
    def i_hate_fives(x):
        for i in range(x):
            if i % n == 0:
                print("Buzz!")
                continue
            print(i)
    return i_hate_fives
            

def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> def identity(x):
    ...     return x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    "*** YOUR CODE HERE ***"
    def new_func(x):
        if x < b : 
            return f(x)
        else:
            return g(x)
    return new_func

from functools import reduce
def funception(func_a, start):
    """ Takes in a function (function A) and a start value.
    Returns a function (function B) that will find the product of 
    function A applied to the range of numbers from 
    start (inclusive) to stop (exclusive)

    >>> def func_a(num):
    ...     return num + 1
    >>> func_b1 = funception(func_a, 3)
    >>> func_b1(2)
    4
    >>> func_b2 = funception(func_a, -2)
    >>> func_b2(-3)
    >>> func_b3 = funception(func_a, -1)
    >>> func_b3(4)
    >>> func_b4 = funception(func_a, 0)
    >>> func_b4(3)
    6
    >>> func_b5 = funception(func_a, 1)
    >>> func_b5(4)
    9
    """
    "*** YOUR CODE HERE ***"
    
    def func_b(stop):
        if start < 0:
            return
        elif start > stop:
            return func_a(start)
        else: 
            result = 0
            for num in range(start , stop):
                result += func_a(num)
            return result
                
    return func_b

def match_pairs(lst, fn):
    """
    >>> lst = ["bobby", "frodo", "sally", "kyoko", "beth"]
    >>> def same_last_char(a, b):
    ...     return a[-1] == b[-1]
    >>> sorted(match_pairs(lst, same_last_char)) # sorted is used for testing 
    [['bobby', 'sally'], ['frodo', 'kyoko'], ['kyoko', 'frodo'], ['sally', 'bobby']]
    >>> def same_first_char(a, b):
    ...     return a[0] == b[0]
    >>> sorted(match_pairs(lst, same_first_char))
    [['beth', 'bobby'], ['bobby', 'beth']]
    """
    "*** YOUR CODE HERE ***"
    result = []
    for num1 in lst:
        for num2 in lst:
            if num1 == num2: continue
            if fn(num1 , num2):
                result.append([num1 , num2])
                
    return result
            
            
            
