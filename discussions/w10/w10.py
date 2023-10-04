class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


"""
    • If there is a duplicate of the first item, we will find that the first and second
    items in the list will have the same values (that is, lnk.first == lnk.rest.first).
    We can confidently state this because we were told that the input linked list
    is in sorted order, so duplicates are adjacent to each other. We’ll remove the
    second item from the list.
    Finally, it’s tempting to recurse on the remainder of the list (lnk.rest), but
    remember that there could still be more duplicates of the first item in the rest
    of the list! So we have to recurse on lnk instead. Remember that we have
    removed an item from the list, so the list is one element smaller than before.
    Normally, recursing on the same list wouldn’t be a valid subproblem.
    • Otherwise, there is no duplicate of the first item. We can safely recurse on the
    remainder of the list.
"""

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return
    if lnk.first == lnk.rest.first:
        lnk.rest = lnk.rest.rest
        remove_duplicates(lnk)
    else:
        remove_duplicates(lnk.rest)
