#!/usr/bin/env python3
"""Module for server class"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing start and end indexes for pagination."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


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
        """Returns the appropriate page of the dataset or an empty list if
        input arguments are out of range."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns hypermedia metadata."""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
