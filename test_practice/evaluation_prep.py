from typing import List

def add(a: int, b: int) -> int:
     """Adds two numbers.

    Args:
        a: An integer
        b: another integer
    Returns:
        The sum of the two integers
    """
 
    return a + b
   

def sum_list(numbers: List) -> int:
    """Adds a number of lists.

    Args:
        numbers: A list of integers
    
    Returns:
        A sum of all numbers in list
    """
    sum = 0
    for num in numbers:
        sum += num
    return sum


def count_occurence(words):
    """Returns a dictionary of the occurance of each word
    Args: A list of words
    
    Returns: 