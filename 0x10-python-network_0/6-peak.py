#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    
    Args:
        list_of_integers (list): A list of unsorted integers.
        
    Returns:
        int: A peak element from the list.
    """
    if not list_of_integers:
        return None
    
    left = 0
    right = len(list_of_integers) - 1
    
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return list_of_integers[left]


