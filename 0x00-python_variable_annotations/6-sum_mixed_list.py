#!/usr/bin/env python3
'''
Complex types - mixed list
'''
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    '''
    function sum_mixed_list which takes a list mxd_lst of integers/
    and floats and returns their sum as a float.
    '''
    return sum(mxd_lst)
