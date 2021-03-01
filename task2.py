#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(x):
    lists = x
    lists.sort()
    length = len(lists)
    return lists[length - 1]




