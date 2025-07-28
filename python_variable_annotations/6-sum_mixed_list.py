#!/usr/bin/env python3
from typing import List, Union

"""
Module for summing a list of integers and floats.

Functions:
    sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
        Returns the sum of a list containing integers and floats.
"""

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst: The list of integers and floats to sum.

    Returns:
        float: The sum of all numbers in the list.
    """
    return sum(mxd_lst)
