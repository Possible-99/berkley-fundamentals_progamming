"""
The object the for loop iterates over must be an iterable! An iterable is a way of representing explicit sequences (like lists or strings) as well as implicit sequences (like the natural numbers 1, 2, 3, ...).

This means the object you want to use a for loop on must implement the iterable interface. To implement the iterable interface, an object must define an __iter__ method that returns an object that implements the iterator interface.

an object must define a __next__ method to compute and return the next element in the sequence. If the iterator exhausts the sequence, it raises StopIteration

An iterable object can create an arbitrary amount of iterator objects. In addition, the iterators are independent of each other; in other words they can have a different position in the sequence.


An iterable is like a book (one can flip through the pages) and an iterator is a bookmark (saves the position and can locate the next page). Calling __iter__ on a book gives you a new bookmark independent of other bookmarks, but calling __iter__ on a bookmark gives you the bookmark itself, without changing its position at all.

Eg : 
class AnIterator:
    def __init__(self):
        self.current = 0

    def __next__(self):
        if self.current > 5:
            raise StopIteration
        self.current += 1
        return self.current

    def __iter__(self):
        return self
        
#>>> for num in AnIterator():
...     print(num)

t = AnIterator()
t = iter(t) # iter(t) is the same as t.__iter__()
try:
    while True:
        # next(t) is the same as t.__next__()
        print(next(t))
except StopIteration as e:
    pass

"""


class Str:
    "*** YOUR CODE HERE ***"
    
    def __init__(self , s):
        self.s = s
        # We want it to be a object variable
        self.idx = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx >= len(self.s):
            raise StopIteration
        char = self.s[self.idx] 
        self.idx += 1
        return char

"""
An iterator is a class with __next__ and __iter__ explicitly defined, but a generator can be written as a mere function with a yield in it.
__iter__ in an iterator uses return, but a generator uses yield.
A generator "remembers" its state for the next __next__ call. Therefore, the first __next__ call works like this:

Enter the function, run until the line with yield.
Return the value in the yield statement, but remember the state of the function for future __next__ calls.
And subsequent __next__ calls work like this:

Re-enter the function, start at the line after yield, and run until the next yield statement.
Return the value in the yield statement, but remember the state of the function for future __next__ calls.

It's like putting a breakpoint




Why does this iterable work without defining a __next__ method?

The for loop only expects the object returned by __iter__ to have a __next__ method. The __iter__ method is a generator function because of the yield statement in the body. Therefore, when __iter__ is called, it returns a generator object, which you can call __next__ on.


Yield in generators functions like a return statement

"""
        
    
def generator():
    # >>> g # what type of object is this?
    # <generator object generator at 0x102a783c0>
    """
    >>> g = generator()
    >>> g == iter(g) # equivalent of g.__iter__()
    True
    >>> next(g) # equivalent of g.__next__()
    Starting here
    Before yield
    0
    >>> next(g)
    After yield
    Before yield
    1
    >>> next(g)
    After yield
    Before yield
    2
    """
    print("Starting here")
    i = 0
    while i < 6:
        print("Before yield")
        yield i
        print("After yield")
        i += 1

        


def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n >= 0 : 
        yield n
        n -= 1
        
    
    
class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    #No need of __next__ method with generators
    def __init__(self , n):
        self.n = n

    def __iter__(self):
        while self.n >= 0 : 
            yield self.n
            self.n -= 1
            
            
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]
    >>> m = scale([1,2,3,4,5], 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    
    for i in range(len(s)):
        s[i] *= k
        yield s[i]
        
        
def pairs(lst):
    """
    >>> type(pairs([3, 4, 5]))
    <class 'generator'>
    >>> for x, y in pairs([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    "*** YOUR CODE HERE ***"
    for i in lst:
        for j in lst:
            yield (i , j)
