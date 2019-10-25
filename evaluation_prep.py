from typing import List


def add(a: int, b: int) -> int:
    return a + b

def sum_list(numbers: List) -> int:
    sum = 0
    for num in numbers:
        sum += num
    return sum
