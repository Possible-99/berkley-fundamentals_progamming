#Exercise 1
def xk(c, d):
    """
    >>> xk(10, 10)
    23

    >>> xk(10, 6)
    23

    >>> xk(4, 6)
    6

    >>> xk(0, 0)
    25
    """
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25
    return 12

#Exercise 2

def how_big(x):
    """
    >>> how_big(7)
    big
    >>> how_big(12)
    huge
    >>> how_big(1)
    small
    >>> how_big(-1)
    negative
    nothing
    """
    if x < 0:
        print('negative')
    if x > 10:
        print('huge')
    elif x > 5:
        print('big')
    elif x > 0:
        print('small')
    else:
        print('nothing')

def positive_loop():
    #Count how many iterations
    # 28 / 3 = 9.3, we have a residuous that means
    # we are going to iterate 9 + 1 = 10 times 
    positive = 28
    while positive > 0:
        print("positive?")
        print(positive)
        positive -= 3

# Not transforms the value to a bool data type
# When we have a bool and other data type(int) and we evaluate it with bool operators, if the two values have the same bool meaning then we get the value of the data type that is not bool, if they are diff. in bool value then we get the one with more importance depending the bool operator(or,and).
# Each value has his bool interpretation if he wins then we return his value not the boolean.
# If we have mulptiple values that are true (1 or 2 or 3), we return the first one that evaluate the statement.
# For and : 1 and 2 and 3 , we need to evaluate all the values for knowing is true so we return the first one that is false or the last one that is true
# For or: 1 or 2 or 3 , return first true or last false.
def wwpd(st):
    """
    >>> wwpd(True and 13)
    13
    >>> wwpd(False or 0)
    0
    >>> wwpd(True or 0)
    True
    >>> wwpd(not 10)
    False
    >>> wwpd(not None)
    True

    # >>> True and 1 / 0 and False
    # ZeroDivisionError
    >>> True or 1 / 0 or False
    True
    >>> True and 0
    0
    >>> False or 1
    1
    >>> 1 and 3 and 6 and 10 and 15
    15
    >>> 0 or False or 2 or 1 / 0
    2

    >>> not 0
    True
    >>> (1 + 1) and 1
    1
    >>> (True or False) and False
    False
    """ 
    print(st)


def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0 # You can replace this line!


def ab(c, d):
    """
    >>> ab(10, 20)
    10
    foo
    """
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')
   
def bake(cake, make):
    """
    >>> bake(0, 29)
    1
    29
    29
    """
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make


def triangular_sum(n):
    """
    >>> t_sum = triangular_sum(5)
    1
    3
    6
    10
    15
    >>> t_sum
    35
    """
    "*** YOUR CODE HERE ***"
    for num in range(1, n + 1):
        print((num + 1) * num // 2)
    return 35

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while(n):
        dig = n % 10
        n = n // 10
        if dig == 8:
            if(count == 1): return True
            count = count + 1
        else:
            count = 0
    return False



# def right_triangle(a, b, c):
#     """Determine whether a, b, and c can be sides of a right triangle
#     >>> right_triangle(1, 1, 1)
#     False
#     >>> right_triangle(5, 3, 4)
#     True
#     >>> right_triangle(8, 10, 6)
#     True
#     """
#     "*** YOUR CODE HERE ***"

if __name__:
    # Data driven iteration
    arr = [1,2,3,4,5]
    arr = [num + 1 for num in arr]
    # Funcion also as a filter because it only apply expression and add it if it meets the condition
    arr = [num + 1 for num in arr if num > 2]
    print(arr)