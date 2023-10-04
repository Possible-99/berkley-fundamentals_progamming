class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

def test_empty(link):
    if link is Link.empty:
        print('This linked list is empty!')
    else:
        print('This linked list is not empty!')
        
# We can change to None in rest = empty and it would be easier to know if is empty
test_empty(Link(2).rest)

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')
    

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)


def q1():
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> link.first
    1
    >>> link.rest.first
    2
    >>> link.rest.rest.rest is Link.empty
    True
    >>> link.first = 9001
    >>> link.first
    9001
    >>> link.rest = link.rest.rest
    >>> link.rest.first
    3
    >>> link = Link(1)
    >>> link.rest = link
    >>> link.rest.rest.rest.rest.first
    1
    >>> link = Link(2, Link(3, Link(4)))
    >>> link2 = Link(1, link)
    >>> link2.first
    1
    >>> link2.rest.first
    2
    >>> print_link(link2) # Look at print_link in lab09.py
    <1 2 3 4>
    """
    
    
def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    >>> print_link(list_to_link([4]))
    <4>
    """
    "*** YOUR CODE HERE ***"
    return helper_lst(0 , lst)

def helper_lst(idx , lst):
    if idx >= len(lst): return Link.empty

    return Link(lst[idx] , helper_lst(idx + 1 , lst))

# How to do this?
# def reverse(link):
#     """Returns a Link that is the reverse of the original.

#     >>> print_link(reverse(Link(1)))
#     <1>
#     >>> link = Link(1, Link(2, Link(3)))
#     >>> new = reverse(link)
#     >>> print_link(new)
#     <3 2 1>
#     >>> print_link(link)
#     <1 2 3>
#     """
#     "*** YOUR CODE HERE ***"

#     if not link.rest:
#         # print(link.first)
#         return Link(link.first)
    
#     new_node = Link(link.first , link.rest)
#     new_head= reverse(link.rest)
#     new_node.rest.rest = new_node 
#     new_node.rest = Link.empty
#     return new_head


def avoid_keyerror(dictionary, key):
    """ Returns the value associated with key in dictionary. If key 
    does not exist in the dictionary, print out 'Avoid Exception' and
    map it to the string 'no value'.

    >>> d = {1: 'one', 3: 'three', 5: 'five'}
    >>> avoid_keyerror(d, 3)
    'three'
    >>> avoid_keyerror(d, 4)
    Avoid Exception
    >>> d[4]
    'no value'
    """
    "*** YOUR CODE HERE ***"
    try:
        return dictionary[key]
    except:
        print("Avoid Exception")
        dictionary[key] =  'no value'
        