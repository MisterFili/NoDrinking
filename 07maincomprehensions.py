#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Let?s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even
elements of this list in it.
"""


def main():
    random_num = [77, 44, 2, 3, 42, 34, 43, 4, 8, 9, 86]
    dog = [item for item in random_num if item % 2 == 0]
    print(dog)


if __name__ == "__main__":
    main()
