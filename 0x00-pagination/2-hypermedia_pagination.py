#!/usr/bin/env python3
"""
The index_range function for pagination with CSV data
"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """
    Calculate the start and end indexes for a given page page size.
    This function takes two arguments, page and page_size, and calculate
    the range of indexes to return the specified pagenation parameters

    Args:
        page (int): Page number, which si 1-indexed.
        page_size (int): The number of items per page.

    Returns:
        turple: A turple containing two integers, the start index (inclusive)
        and an end index (inclusive).

    raises:
       ValueError: If page or page_size is not positive integer.
    """

    if (not isinstance(page, int) or
            not isinstance(page_size, int) or
            page <= 0 or
            page_size <= 0):

        raise ValueError("Both page and page size must be positive integers.")

    start_index, end_index = (page - 1) * page_size, page * page_size
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
        """
        Read CSV file to load dataset
        Check if the provided page, page_size are positive integers.

        Use the index_range function to calculate the start and end indexes
        for pagination.

        Retrieve the appropriate page of data by slicing the dataset using
        the calculated index.

        Returns:
            Page: Page of data or an empty list if the args are out of range
        """

        if (not isinstance(page, int) or
                not isinstance(page_size, int) or
                page <= 0 or
                page_size <= 0):
            # Return an empty list if args are invalid
            return []

        # Get the start index and end index using the index_range function
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset and return the appropriate page
        dataset = self.dataset()
        if start_index >= len(dataset):

            # Return an empty list if the start index is out of range
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve paginated data and create hypermedia response.

        Args:
            page (int): Page number, 1-indexed. Default to 1.
            page_size (int): The number of items per page. default to 10.

        Returns:
            Dict: A dictionary containing hypermedia information:
                "page_size": Length of the returned dataset page
                "page": The current page number
                "data": The dataset page.
                "next_page": The number of the next page or None
                if no next page.
                "prev_page": The number of the previous page or
                None if no prev page.
                "total_pages": The total number of pages in the dataset
        raises:
           ValueError: If page or page_size is not a positive integer.
        """

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # Determine the next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Create the dictionary
        hyper_dict = {
                "page_size": len(page_data),
                "page": page,
                "data": page_data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
        }

        return hyper_dict
