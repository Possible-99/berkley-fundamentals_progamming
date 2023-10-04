#We can have more than one data type in a list
"""
>>> [1,2,3]
[1, 2, 3]
>>> ["frog", 3, 3.1415]
['frog', 3, 3.1415]
>>> [True, [1, 2], 42]
[True, [1, 2], 42]
"""

#Operations
"""
>>> x = [1,2,3]    # assign them to variables
>>> len(x)         # get their length, i.e., the number of elements in them
3
>>> x + [4,5]      # + is concatenation
[1, 2, 3, 4, 5]
>>> [1,2] * 3        # * is replication
[1, 2, 1, 2, 1, 2]
>>> len([1,2] * 3)
6
"""

#In operator
"""
#In  operator: Operates entire list and produce boolean that tell you if the element is in the list.

>>> 2 in [1,2,3]
True
>>> "frog" in [1,2,3]
False
>>> [1,2] in [1,2,3]
False
>>> [1,2] in [[1,2],3]
True
"""

#List Comprehensions

"""
Create a new list where we have only even elements, and we apply a operation: multiply them by 2.
>>> [i**2 for i in [1, 2, 3, 4] if i%2 == 0]
[4, 16]
"""

# HOF gives arguments access to his functions.
# def leq_maker(c):
#     def leq(val):
#         return val <= c
#     return leq

# print([x for x in range(7) if leq_maker(3)(x)])

#Map, reduce and filter. (function , sequence, optional_container)

def map_test():
    INCR = 2
    def inc(x):
        return x+INCR

    def mymap(fun, seq):
        return [fun(x) for x in seq]

    result = mymap(inc, [5, 6, 7])
    #result2 = map(inc , [5, 6, 7])
    print(result)


def filter_test():
    def isPositive(number):
        return number >= 0
    numbers = [-1, 1, -2, 2, -3, 3, -4, 4]
    positive_nums = list(filter(isPositive, numbers))
    print(positive_nums)

def reduce():
    multiplicative_identity = 1
    nums = [4, 9, 16, 25, 36]
    def sqrtProd(x, y):
        return x * y ** .5

    print(reduce(sqrtProd, nums, multiplicative_identity))

# Exercise 1: Classify elements

def odd_even(x):
    """Classify a number as odd or even.

    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    "*** YOUR CODE HERE ***"
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'

def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    "*** YOUR CODE HERE ***"
    return list(map(odd_even, s))

    

def if_this_not_that(i_list, this):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    "*** YOUR CODE HERE ***"
    def check_value(element):
        if(element > this):
            return element 
        else:
            return "that"
    
    # result = map(check_value , i_list)
    # for x in result: print(x)

    for elem in i_list:
        if elem <= this:
            print("that")
        else:
            print(elem)



def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

     >>> shuffle(range(6))
     [0, 3, 1, 4, 2, 5]
     >>> suits = ['H', 'D', 'S', 'C']
     >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
     >>> cards[:12]
     ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
     >>> cards[26:30]
     ['7S', '7C', '8H', '8D']
     >>> shuffle(cards)[:12]
     ['AH', '7S', 'AD', '7C', 'AS', '8H', 'AC', '8D', '2H', '8S', '2D', '8C']
     >>> shuffle(shuffle(cards))[:12]
     ['AH', '4D', '7S', '10C', 'AD', '4S', '7C', 'JH', 'AS', '4C', '8H', 'JD']
     >>> cards[:12] # Should not be changed
     ['AH', 'AD', 'AS', 'AC', '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C']
     """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    "*** YOUR CODE HERE ***"
    # p1 , p2, p3 = 0 , len(cards) // 2 , 0
    # size = len(cards)
    # res = []

    # while p3 < size:
    #     if(p3 % 2 == 0):
    #         res.append(cards[p1])
    #         p1 += 1
    #     else:
    #         res.append(cards[p2])
    #         p2 += 1
    #     p3 += 1
    # return res
    
    # When we have a problem where we iterate until the half, we can optimize it by not iterating the other half and taking advantage with arithmetic and adding the two elements on the one half pass.
    half = len(cards) // 2
    shuffled = []
    for i in range(half):
        shuffled.append(cards[i])
        shuffled.append(cards[i + half])
    return shuffled
            

    

def pairs(n):
    """Returns a new list containing two element lists from values 1 to n
    >>> pairs(1)
    [[1, 1]]
    >>> x = pairs(2)
    >>> x
    [[1, 1], [2, 2]]
    >>> pairs(5)
    [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    >>> pairs(-1)
    []
    """
    "*** YOUR CODE HERE ***"
    
    return [[x,x] for x in range(1, n + 1)]


def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> def fn(x):
    ...     return x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    # For checking ranges is better to put it like math 
    return [ [x , fn(x)] for x in seq if lower <= fn(x) and fn(x) <= upper]