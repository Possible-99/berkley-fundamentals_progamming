
#Lists review
def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    >>> matrix4 = [[ 1, -2,  3],
    ...            [-4,  5, -6]]
    >>> matrix5 = [[-1,  2, -3],
    ...            [ 4, -5,  6]]
    >>> add_matrices(matrix4, matrix5)
    [[0, 0, 0], [0, 0, 0]]
    """
    "*** YOUR CODE HERE ***"
    # For nested loops we read it from right to left
    return [[ x[row][col] + y[row][col] for col in range(len(x[row])) ] for row in range(len(x))]


# Higher order functions 
# For this exercises is good to think it as inner and outter function

def mul_by_num(factor):
    """
    Returns a function that takes one argument and
    returns the product of factor and that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    "*** YOUR CODE HERE ***"
    
    def mult(x):
        return x * factor
    
    return mult


# The only thing that changes is the boolean function
# So we can reutilize the logic by creating a HOF where we return a function 
# The hof by itself with the call of count is O(n)
# But we can add complexity with the funciton that we pass,
# It can be O(n) where we do a linear check like checking if a number is prime
# Also it can be only a constant function like a condition O(1)
# So HOF -> O(n * n * 1)

def count_cond(mystery_function, n):
    """
    >>> def divisible(n, i):
    ...     return n % i == 0
    >>> count_cond(divisible, 2) # 1, 2
    2
    >>> count_cond(divisible, 4) # 1, 2, 4
    3
    >>> count_cond(divisible, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> def is_prime(n, i):
    ...     return count_cond(divisible, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    i, count = 1, 0
    while i <= n:
         # For mistery_funciton O(n), because it calls again count_cond
            # mystery_function -> count_cond -> divisible  
            #                     O(n)             O(1)
        if mystery_function(n, i):
            count += 1
        i += 1
    return count


# We need to go applying funcitons to x, depending on 1...n
def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def ret_fn(n):
        def ret(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return ret
    return ret_fn



def store_word(secret):
    """
    >>> word_len, guess_word = store_word("cake")
    >>> word_len
    4
    >>> guess_word("corn")
    [True, False, False, False]
    >>> guess_word("come")
    [True, False, False, True]
    >>> guess_word("cake")
    [True, True, True, True]
    >>> word_len, guess_word = store_word("pop")
    >>> word_len
    3
    >>> guess_word("ate")
    [False, False, False]
    >>> guess_word("top")
    [False, True, True]
    >>> guess_word("pop")
    [True, True, True]
    """
    "*** YOUR CODE HERE ***"
    size = len(secret)
    
    def guess_word(word):
        # l = [False] * size
        # for i in range(size):
        #     if word[i] == secret[i] : l[i] = True
        
        # return l
        return [word[i] == secret[i] for i in range(len(word))]

    return size , guess_word


# matrix4 = [[ 1, -2,  3], [-4,  5, -6]]
# matrix5 = [[-1,  2, -3], [ 4, -5,  6]]


# print(add_matrices(matrix4 , matrix5))