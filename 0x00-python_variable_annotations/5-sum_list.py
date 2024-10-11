#!/usr/bin/env python3
from typing import List
"""
This module takes sums a list of floats as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Function returns sum of a list of floats, as float

    Args:
    input_list (List): the list to be summed

    Returns:
    float: the sum
    """
    rslt = 0.00
    for i in input_list:
        rslt += i
    return rslt
