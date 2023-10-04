# Diner ADT
def make_diner(name):
    """ Diners are represented by their name and the number of free tables they have."""
    return [name, 0]

def num_free_tables(diner):
    return diner[1]

def name(diner):
    return diner[0]
# You will implement add_table and serve which are part of the Diner ADT

def add_table(diner):
    """
    >>> din = make_diner("Croads")
    >>> num_free_tables(din)
    0
    >>> add_table(din)
    >>> add_table(din)
    >>> num_free_tables(din)
    2
    """
    "*** YOUR CODE HERE ***"
    diner[1] += 1

def serve(diner, group):
    """
    >>> din = make_diner("Cafe 3")
    >>> add_table(din)
    >>> g1 = make_group("Vandana's Group")
    >>> g2 = make_group("Shreya's Group")
    >>> serve(din, g1)
    >>> status(g1)
    'eating'
    >>> num_free_tables(din)
    0
    >>> serve(din, g2)
    'table not free'
    >>> status(g2)
    'waiting'
    """
    "*** YOUR CODE HERE ***"
    if num_free_tables(diner) > 0:
        diner[1] -= 1
        group[1] = 'eating'
    else:
        return 'table not free'

# Group ADT
def make_group(name):
    """ Groups are represented by their name and their status."""
    return [name, 'waiting']

def name(group):
    return group[0]

def status(group):
    return group[1]

def start_eating(group, diner):
    group[1] = 'eating'

# You will implement finish_eating which is part of the Group ADT    

def finish_eating(group, diner):
    """
    >>> din = make_diner("Foothill")
    >>> add_table(din)
    >>> g1 = make_group("Nick's Group")
    >>> serve(din, g1)
    >>> num_free_tables(din)
    0
    >>> finish_eating(g1, din)
    >>> num_free_tables(din)
    1
    >>> status(g1)
    'finished'
    >>> finish_eating(g1, din) # g1 has already finished eating so this should do nothing
    >>> num_free_tables(din)
    1
    >>> status(g1)
    'finished'
    """
    "*** YOUR CODE HERE ***"

    if status(group) != 'finished':
        group[1] = 'finished'
        add_table(diner)


full_roster = {
    "Manny Machado" : "Dodgers",
    "Yasiel Puig" : "Dodgers",
    "Aaron Judge" : "Yankees",
    "Clayton Kershaw" : "Dodgers",
    "Giancarlo Stanton" : "Yankees"
}

full_stats = {
    "Manny Machado": ["SO", "1B", "3B", "SO", "HR"],
    "Yasiel Puig": ["3B", "3B", "1B", "1B", "SO"],
    "Aaron Judge": ["SO", "HR", "HR", "1B", "SO"],
    "Clayton Kershaw": ["1B", "SO", "SO", "1B", "SO"],
    "Giancarlo Stanton": ["HR", "SO", "3B", "SO", "2B"],
}

def get_team(player):
    """Returns team that the provided player is a member of.

    >>> get_team("Manny Machado")
    'Dodgers'
    >>> get_team("Aaron Judge")
    'Yankees'
    """
    "*** YOUR CODE HERE ***"
    return full_roster[player]
    

def get_stats(player):
    """Returns the statistics associated with the provided player.
    >>> get_stats("Manny Machado")
    ['SO', '1B', '3B', 'SO', 'HR']
    >>> get_stats('Aaron Judge')
    ['SO', 'HR', 'HR', '1B', 'SO']
    """
    "*** YOUR CODE HERE ***"
    return full_stats[player]
    