#!/usr/bin/env python3
from typing import  List
"""
Module for summing a list of floating point numbers.

"""


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floating point numbers.

    Args:
        input_list (list[float]): The list of floats to sum.

    Returns:
        float: The sum of all numbers in the list.
    """
    return sum(input_list)
