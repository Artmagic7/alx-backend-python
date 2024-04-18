#!/usr/bin/env python3
'''Module of Task 8.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Design a multiplier function.
    '''
    return lambda x: x * multiplier
