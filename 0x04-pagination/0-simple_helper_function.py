#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    The function should return a tuple of size two containing/
    a start index and an end index corresponding to the range/
    of indexes to return in a list for those particular pagination parameters.
    '''
    if page and page_size is not None:
        start_index = (page - 1) * page_size
        end_index = page_size + start_index
    return (start_index, end_index)
