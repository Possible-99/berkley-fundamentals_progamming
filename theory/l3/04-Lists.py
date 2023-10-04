sentence = "Welcome to C88C!"
numbers = range(10)

for letter in sentence:
    print(letter)

# W
# e
# l
# c
# o
# m
# e
#
# t
# o
#
# C
# 8
# 8
# C
# !
numbers
# range(0, 10)
total = 0
for num in numbers:
    print(num)
    total += num

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
total
# 45


sentence
# 'Welcome to C88C!'
sentence[0]
# 'W'
len(sentence)
# 16
sentence[16]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
sentence[15]
# '!'
sentence[len(sentence) - 1]
# '!'
numbers = range(0, 10)
numbers
# range(0, 10)
len(numbers)
# 10
numbers[0]
# 0
numbers[9]
# 9
numbers[10]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: range object index out of range
numbers = range(1, 11)
len(numbers)
# num      numbers
len(numbers)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'lwn' is not defined
len(numbers)
# 10
numbers[0]
# 1
numbers[9]
# 10
list(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

courses = ['CS88', 'DATA8', 'POLSCI2', 'PHILR1B']
for course in courses:
    print('I am taking ' + course)

# I am taking CS88
# I am taking DATA8
# I am taking POLSCI2
# I am taking PHILR1B
len(courses)
# 4
courses[2]
# 'POLSCI2'
list
# <class 'list'>
list(range(2, 7))
# [2, 3, 4, 5, 6]
courses
# ['CS88', 'DATA8', 'POLSCI2', 'PHILR1B']
courses + [ 123 ]
# ['CS88', 'DATA8', 'POLSCI2', 'PHILR1B', 123]
courses = courses + [ 123 ]
courses
# ['CS88', 'DATA8', 'POLSCI2', 'PHILR1B', 123]
for course in courses:
    print('I am taking ' + course)

# I am taking CS88
# I am taking DATA8
# I am taking POLSCI2
# I am taking PHILR1B
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# TypeError: can only concatenate str (not "int") to str
for course in courses:
    print('I am taking ' + str(course))

# I am taking CS88
# I am taking DATA8
# I am taking POLSCI2
# I am taking PHILR1B
# I am taking 123
print(12)
# 12
"Hello C" + 88
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
courses
# ['CS88', 'DATA8', 'POLSCI2', 'PHILR1B', 123]
courses + 'C88C'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate list (not "str") to list
courses + [ 'C88C' ]
# ['CS88', 'DATA8', 'POLSCI2', 'PHILR1B', 123, 'C88C']
1 + 2.4
# 3.4
for c in courses:
    print(c)

# CS88
# DATA8
# POLSCI2
# PHILR1B
# 123
c
# 123
max(range(100))
# 99

t = ()
t
# ()
courses
# ['CS88', 'DATA8', 'POLSCI2', 'PHILR1B', 123]
courses[0] = 'DATAC88C'
courses
# ['DATAC88C', 'DATA8', 'POLSCI2', 'PHILR1B', 123]
t = tuple(courses)
t
# ('DATAC88C', 'DATA8', 'POLSCI2', 'PHILR1B', 123)
t[0]
# 'DATAC88C'
t[3]
# 'PHILR1B'
t[0] = 'CS88'
