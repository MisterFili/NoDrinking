#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Let?s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even 
elements of this list in it.
"""

"""
birth_year = [1990, 1993, 1980, 1996, 2002, 1963]
ages = [2017 - item for item in birth_year]
#2017 minus each item in birth_year

print(ages)
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = [ item for item in a if item % 2 == 0 ]
print(even)