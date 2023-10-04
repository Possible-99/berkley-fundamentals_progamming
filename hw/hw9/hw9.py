# Linked List Class
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

# Notice that this is not part of the Link class.
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

######################
#### Linked Lists ####
######################

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link(88))
    [88]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty : return []
    return [link.first] + link_to_list(link.rest)


def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s) # removes 2, 4
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length) # removes 3
    >>> odd_length
    Link(5, Link(1))
    >>> two_items = Link(6, Link(7))
    >>> every_other(two_items) # removes 7
    >>> two_items
    Link(6)
    >>> singleton = Link(4)
    >>> every_other(singleton) # doesn't remove anything
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
    if s == Link.empty or s.rest == Link.empty : return 
    s.rest = s.rest.rest
    every_other(s.rest)
    


    


def slice_link(link, start, end):
    """Slices a Link from start to end (as with a normal Python list).

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> new
    Link(1, Link(4, Link(1)))
    >>> link2 = slice_link(Link(1), 0, 1)
    >>> link2
    Link(1)
    >>> link3 = slice_link(Link.empty, 0, 0)
    >>> link3
    ()
    """
    "*** YOUR CODE HERE ***"
    return slice_helper(0 , start , end, link)

def slice_helper(idx , start ,end, link):
    if idx >= end : return Link.empty

    if idx >= start:
        new_node = Link(link.first)
        new_node.rest = slice_helper(idx + 1 , start , end , link.rest)
        return new_node
    else:
        return slice_helper(idx + 1 , start , end , link.rest)

def deep_map(f, link):
    """Return a Link with the same structure as link but with fn mapped over
    its elements. If an element is an instance of a linked list, recursively
    apply f inside that linked list as well.

    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print_link(s)
    <1 <2 3> 4>
    >>> print_link(deep_map(lambda x: x * x, s))
    <1 <4 9> 16>
    >>> print_link(s) # unchanged
    <1 <2 3> 4>
    >>> t = Link(s, Link(Link(Link(5))))
    >>> print_link(t)
    <<1 <2 3> 4> <<5>>>
    >>> print_link(deep_map(lambda x: 2 * x, t))
    <<2 <4 6> 8> <<10>>>
    """
    "*** YOUR CODE HERE ***"
    
    if link == Link.empty : return
    
    if isinstance(link.first , Link):
        deep_map(f , link.first)
    else:
        
        link.first = f(link.first)
    deep_map(f , link.rest)
        
    return link
    

    