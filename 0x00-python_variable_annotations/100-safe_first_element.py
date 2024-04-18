#!/usr/bin/env python3
''' Duck typing - 1st element of a sequence
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Augmenting following code with the correct
    duck-typed annotation
    '''
    if lst:
        return lst[0]
    else:
        return None
