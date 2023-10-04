"""
    An abstract data type consists of two types of functions:
    • Constructors: functions that build the abstract data type.
    • Selectors: functions that retrieve information from the data type.
    
    Abstract violation
    You should never assume anything about how the constructors and selectors for an abstract data type are implemented. Doing so is called a data abstraction violation.
    We assumed rationals were represented as lists instead of accessing their elements using the selectors.

    Eg:
    
    def rational(n, d):
        return [n, d]
    >>> frac1 = rational(3, 4)
    >>> frac2 = rational(5, 6)
    >>> frac1[0] * frac2[0]
"""

def make_discussion(ta, time, students):
    return [ta, time, students]
def get_ta(disc):
    return disc[0]
def get_time(disc):
    return disc[1]
def get_students(disc):
    return disc[2]


def add_student(disc, student):
    """ Adds a student to this discussion.
    >>> disc = make_discussion("Alex", 4, ["Srinath", "Brian
    "])
    >>> new_disc = add_student(disc, "Sophia")
    >>> get_students(new_disc)
    ["Srinath", "Brian", "Sophia"]
    >>> get_students(disc)
    ["Srinath", "Brian"]
    """
    return make_discussion(get_ta(disc) , get_time(disc) , get_students(disc).append(student))


"""
def check_start(disc1, disc2):
    return get_time(disc1) == get_time(disc2):
def print_students(disc):
    for student in get_students(disc2):
        print(student)
def print_duplicates(disc1, disc2):
    students_1, students_2 = get_students(disc1),
    get_students(disc2)
    for i in range(len(students_1)):
        if students_1[i] in students_2:
        print(students_1[i])
"""


def near_thirty(city, diff):
    city_latitude = get_lat(city)
    return abs(city_latitude - 30) <= diff or abs(city_latitude + 30) <= diff

