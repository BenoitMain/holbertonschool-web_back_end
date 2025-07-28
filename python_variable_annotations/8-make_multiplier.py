#!/usr/bin/env python3
from typing import Callable

"""
Module for creating multiplier functions.

Functions:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
        Returns a function that multiplies a float by the given multiplier.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable: Returns its product with multiplier.
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
