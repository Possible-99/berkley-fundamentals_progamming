#Trees

# Tree Class
class Tree:
    def __init__(self, value, branches=()):
        self.value = value
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.value, branches_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.value) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def is_leaf(self):
        return not self.branches


#Wrong test cases
# # Q1
# def search(t, value):
#     """Searches for and returns the Tree whose value is equal to value if
#     it exists and None if it does not. Assume unique values.

#     >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
#     >>> search(t, 10)
#     >>> search(t, 5)
#     Tree(5)
#     >>> search(t, 1)
#     Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
#     >>> search(t, 7)
#     Tree(7)
#     """
#     "*** YOUR CODE HERE ***"
#     if t.is_leaf():
#       if t.value != value : return None

#     if t.value == value : 
#       print(t.value)
#       return t
    
#     for b in t.branches :
#       value = search(b , value)
#       if value != None : return value
    
#     return None



# # Q2
def cumulative_sum(t):
    """Return a new Tree, where each value is the sum of all values in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    "*** YOUR CODE HERE ***"

    if t.is_leaf():
      return Tree(t.value)

    root = Tree(t.value)

    for b in t.branches : 
      root.branches.append(cumulative_sum(b))

    root.value += sum([b.value for b in root.branches])
    
    return root



      


# #Q3
def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    def add_leaves(t, v):
        "*** YOUR CODE HERE ***"
        def helper(t, v, depth):
            # base case
            if t.is_leaf():
                for i in range(depth):
                    t.branches.append(Tree(v))
                return

            # check every branch
            for b in t.branches:
                helper(b, v, depth + 1)
            

            # check current node
            for i in range(depth):
                t.branches.append(Tree(v))

        helper(t, v, 0)
    add_leaves(t, 10)


# t1 = Tree(1, [Tree(3)])
# t2 = Tree(2, [Tree(5 , [Tree(4)]), Tree(6)])
# t3 = Tree(3, [t1, Tree(0), t2])

# print(t3)