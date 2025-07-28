#!/usr/bin/env python3
import math

"""
Module for computing the floor of a floating point number.

Functions:
    floor(n: float) -> int: Returns the floor of a float.
"""


def floor(n: float) -> int:
    """
    Returns the floor of a floating point number.

    Args:
        n (float): The number to floor.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
