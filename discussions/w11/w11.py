"""
A tree is considered a
recursive data structure because every branch from a node is also a tree.
Contrary to our ideas of a tree, in computer science, a tree branches downward.
The root of a tree starts at the top, and the leaves are at the bottom
"""


class Tree:
    def __init__(self, value, branches=()):
        for b in branches:
            assert isinstance(b, Tree)
        self.value = value
        self.branches = list(branches)
    def is_leaf(self):
        return not self.branches
    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
            return 'Tree({0}{1})'.format(self.value, branches_str)
    
    
