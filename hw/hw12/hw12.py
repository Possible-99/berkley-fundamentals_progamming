class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.start = start
        self.end = end
        self.curr = start

    def __next__(self):
        "*** YOUR CODE HERE ***"
        if self.curr > self.end : 
            raise StopIteration
        number = self.curr
        self.curr += 1
        return number

    def __iter__(self):
        "*** YOUR CODE HERE ***"
        self.curr = self.start
        return self
    
    
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        yield n
        if n % 2 == 0 : 
            n //= 2
        else :
            n = n * 3 + 1
    yield n 
    
    
def generate_perms(lst):
    """
    Generates the permutations of lst one by one.
    >>> perms = generate_perms([1, 2, 3])
    >>> hasattr(perms, '__next__')
    True
    >>> p = list(perms)
    >>> p
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    "*** YOUR CODE HERE ***"
    perms = []
    while True:
        # perms.append(lst)
        yield lst
        idx = -1
        for i in range(len(lst) - 2, -1 , -1):
            if lst[i] < lst[i + 1] : 
                idx = i
                break

        if idx == -1:
            break

        bigger = 0
        for i in range(len(lst) - 1, -1 , -1):
            if lst[i] > lst[idx] : 
                bigger = i
                break

        lst[idx] , lst[bigger] = lst[bigger] , lst[idx]

        lst = reverseArr(lst , idx + 1)

def reverseArr(lst , start):
    end = len(lst) - 1
    while start < end:
        lst[start] , lst[end] = lst[end] , lst[start]
        start += 1
        end -= 1
    return lst

    