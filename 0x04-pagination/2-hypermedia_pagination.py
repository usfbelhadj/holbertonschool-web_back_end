#!/usr/bin/env python3
"""
pagination
"""

import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        get_page
        '''
        assert type(page) == int and page > 0 and type(
            page_size) == int and page_size > 0
        indexes, page_indexes = index_range(page, page_size)
        if indexes > len(self.dataset()):
            return []
        res = self.dataset()
        return res[indexes:page_indexes]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        '''
        get_hyper
        '''
        indexes, page_indexes = index_range(page, page_size)
        if indexes > 0:
            prev_page = page - 1
        else:
            prev_page = None
        pages = math.ceil(len(self.dataset()) / page_size)

        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                "next_page": page + 1 if page + 1 < pages else None,
                "prev_page": page - 1 if page > 1 else None,
                'total_pages': pages}
