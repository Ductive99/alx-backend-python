#!/usr/bin/env python3
"""Task 7"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """Returns a tuple from string k and number v"""
    return (k, float(v**2))
