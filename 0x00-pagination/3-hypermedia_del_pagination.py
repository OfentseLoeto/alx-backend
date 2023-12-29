#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        pass

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a hypermedia page from the indexed dataset.

        Parameters:
        - index (int, optional): The start index of the requested page.
          If not provided, set to None.
        - page_size (int, optional): The size of the requested page.
                                     Defaults to 10.

        Returns:
        Dict: A dictionary containing the hypermedia page information.
              The dictionary has the following key-value pairs:
              - 'index': The current start index of the returned page.
              - 'data': The actual page data from the dataset.
              - 'page_size': The current page size.
              - 'next_index': The next index to query for the subsequent page.

        Raises:
        AssertionError: Raised if the provided index is out of range.
        """
        assert index is None or 0 <= index < len(self.__indexed_dataset)

        data_page = []
        next_index = index + page_size
        dataset_length = len(self.__indexed_dataset)

        for i in range(index, min(next_index, dataset_length)):
            # Check if the index is present in the dataset
            if i in self.__indexed_dataset:
                data_page.append(self.__indexed_dataset[i])

        return {
            'index': index,
            'data': data_page,
            'page_size': page_size,
            'next_index': min(next_index, dataset_length)
        }
