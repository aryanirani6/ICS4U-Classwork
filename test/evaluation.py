from typing import List, Dict
def average_marks(a: float, b:float, c: float)->float:
    """Finds the average of three marks

        Args:
            a: a float number
            b: another float number
            c: another float number
        
        Return:
            Average of float numbers
    """
    sum_average = (a + b + c)/3
    return sum_average

def number_occurences(number: List[int]) -> int:
    """Find the number of pieces of wood in an invenotry at a specific length

        Args:
            number: List of integers

        Returns: Number of occurences of of that piece of wood
    """
    occurences = []
    count = occurences.count()
    return count

def occurences_times(numbers: List[int]) -> Dict:
    """ Returns a dictionary of occurence of each number

        Args:
            numbers: list of numbers
        
        Returns: A dictionary with the key being the length and value being the number of occurence
    """
    occured = {}
    for num in numbers:
        if num in occured.keys():
            occured[num] += 1
        else:
            occured[num] = 1
    return occured

def reverse_occurences(numbers1: Dict) -> List:
    """ Returns quantity of that board length from inventory

    Args:
        numbers1: A dictionary with integers
    Returns:
        The quantity of that board length in the inventory
    
    """
    
    occur = []
    for numbers1.key() in occur:
        if numbers1[key] in occurences.key:
            numbers1[key] += 1
        else:
            numbers1[key] = 1
    return occur
    






