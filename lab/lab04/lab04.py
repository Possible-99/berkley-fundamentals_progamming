import tracemalloc
from timeit import default_timer as timer
"""
    # Common ways of using lambda:
    assign lambda to variables (foo = lambda x: x)
    pass them in to other functions (bar(lambda x: x))
    return them as the results of other functions (return lambda x: x)
    return them as the results of other lambdas (lambda x: lambda y: x + y)
    
    The difference between lambda expressions and def statement is that lambda expressions do not create
    any new bindings in the environment.
"""


def question1():
    """
    #>>> lambda x: x  # A lambda expression with one parameter x
    #<function <lambda> at 0x1012b0550>
    >>> a = lambda x: x  # Assigning the lambda function to the name a
    >>> a(5)
    5
    >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
    3
    >>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
    >>> c = b(88)
    >>> c()
    88
    >>> d = lambda f: f(4)  # They can have functions as arguments as well.
    >>> def square(x):
    ...     return x * x
    >>> d(square)
    16

    >>> z = 3
    >>> e = lambda x: lambda y: lambda: x + y + z
    >>> e(0)(1)()
    4
    >>> f = lambda z: x + z
    
    
    
    >>> higher_order_lambda = lambda f: lambda x: f(x)
    >>> g = lambda x: x * x
    >>> higher_order_lambda(g)(2)
    4

    >>> call_thrice = lambda f: lambda x: f(f(f(x)))
    >>> call_thrice(lambda y: y + 1)(0)
    3

    >>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
    >>> one_thousand = print_lambda(1000)
    1000

    >>> one_thousand
    """



def mul_by_num(num):
    """
    Returns a function that takes one argument and returns num
    times that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    "*** YOUR CODE HERE ***"
    return lambda x : num * x


def compose(f, g):
    """Write a function that takes in 2 single-argument functions, f and g, and returns another lambda function 
    that takes in a single argument x. The returned function should return the output of applying f(g(x)). 
    Hint: The staff solution is only 1 line!

    Return the composition function which given x, computes f(g(x)). 

    >>> add_two = lambda x: x + 2  		# adds 2 to x
    >>> square = lambda x: x ** 2 		# squares x
    >>> a = compose(square, add_two) 	# (x + 2 ) ^ 2
    >>> a(5) 
    49
    >>> mul_ten = lambda x: x * 10 		# multiplies 10 with x
    >>> b = compose(mul_ten, a) 		# ((x + 2 ) ^ 2) * 10
    >>> b(5)
    490
    >>> b(2)
    160
    """
    "*** YOUR CODE HERE ***"
    
    return lambda x : f(g(x))



def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split()
    "*** YOUR CODE HERE ***"
    dic = {}
    for w in message.split():
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1
    return dic
    
    
def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    >>> full_roster = {"bob": "Team A", "barnum": "Team B", "beatrice": "Team C", "bernice": "Team B", "ben": "Team D", "belle": "Team A", "bill": "Team B", "bernie": "Team B", "baxter": "Team A"}
    >>> player_dict = common_players(full_roster)
    >>> dict(sorted(player_dict.items()))
    {'Team A': ['bob', 'belle', 'baxter'], 'Team B': ['barnum', 'bernice', 'bill', 'bernie'], 'Team C': ['beatrice'], 'Team D': ['ben']}
    """
    "*** YOUR CODE HERE ***"
    dic= {}
    #This is better because we mutate the list(inplace)
    # Also in time is better because 
    for key in roster:
        if roster[key] in dic:
            dic[roster[key]].append(key)
        else:
            dic[roster[key]] = [key]
    return dic

    #We create a new list each time
    # for player in roster:
    #     team = roster[player]
    #     if team in result_dict:
    #         result_dict[team] += [player]
    #     else:
    #         result_dict[team] = [player]
    # return result_dict

start = timer()
tracemalloc.start()

full_roster = {"bob": "Team A", "barnum": "Team B", "beatrice": "Team C", "bernice": "Team B", "ben": "Team D", "belle": "Team A", "bill": "Team B", "bernie": "Team B", "baxter": "Team A"}

player_dict = common_players(full_roster)

dict(sorted(player_dict.items()))


print(tracemalloc.get_traced_memory())
 
# stopping the library
tracemalloc.stop()
end = timer()
print(end - start)