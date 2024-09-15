#!/usr/bin/env python3
"""Module contains function that returns pagination range
Imports:
    Typing: Type annotation module
    Tuple: Tuple type annotation
    List: List type anotaton
    Dict: Dict type annotation
    csv: csv module
"""
import csv
from typing import List
from typing import Tuple
from typing import Dict
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function o fthe module

    Args:
        page (_type_): page index
        page_size (_type_): page size of items to display

    Returns:
        _type_: A tiple of both page and page size
    """
    start = (page - 1) * page_size
    end = page * page_size
    page_tuple = (start, end)
    return page_tuple

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
        """Gets specific data
        """
        assert page > 0
        assert page_size > 0
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        my_range = index_range(page, page_size)
        start = my_range[0]
        end = my_range[1]
        csv_list = self.dataset()

        if start >= len(csv_list):
            return []
        return csv_list[start:end]
    

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing hypermedia pagination information.
        """
        assert page > 0
        assert page_size > 0
        assert isinstance(page, int)
        assert isinstance(page_size, int)

        csv_list = self.dataset()
        total_items = len(csv_list)
        total_pages = math.ceil(total_items / page_size)

        start, end = self.index_range(page, page_size)
        data = csv_list[start:end]

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
    