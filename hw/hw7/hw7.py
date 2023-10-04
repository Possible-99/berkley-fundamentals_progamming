"""
    The (simple) way you figure out the running time of a particular while loop is to simply count the cost of each operation in the body of the while loop, and then multiply that cost by the number of times that the loop runs
    O(33n) -> O(n)
"""



def baz(n):
    i = 1
    sum = 0
    # Time : n * 2n -> 2n ** 2 -> n ** 2
    # n 
    while i <= n:
        #  2 * n
        sum += bam(i)
        # 1 
        i += 1
    return sum

def bam(n):
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return sum


def bonk(n):
    sum = 0
    # O (logn)
    while n >= 2:
        # 1
        sum += n
        # 2
        n = n / 2
    return sum


## Exceptions


"""
    
"""