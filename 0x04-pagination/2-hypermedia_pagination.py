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
        assert type(page) == int and page > 0 and type(
            page_size) == int and page_size > 0
        indexes, page_indexes = index_range(page, page_size)
        if indexes > 0:
            prev_page =  page - 1
        else:
            prev_page = None
        pages = math.ceil(len(self.dataset()) / page_size)
        if indexes > len(self.dataset()):
            res = []
            next_page = None
            page_size = 0
            prev_page = page - 1
            return  {'page_size': page_size, 'page': page, 'data':res, 'next_page': next_page , 'prev_page': prev_page, 'total_pages': pages}
        res = self.dataset()

        return  {'page_size': page_size, 'page': page, 'data':res[indexes:page_indexes], 'next_page': page + 1, 'prev_page': prev_page, 'total_pages': pages}