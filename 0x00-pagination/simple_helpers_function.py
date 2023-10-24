#!/usr/bin/env python3
"""
Calculate the start and end index for a given page.
"""


def index_range(page, page_size):
    """
    Calculate the start and end index for a given page
    This function takes two parameters 'page' and pages_size
    and calculate the range of indexes to return for the specified
    pagination parameter.

    Args:
        page (int): The page number, which is 1-indexed.
        page_size (int): The number of items per page.

    Retuns:
        tuple: A tuple containing two integers, the start index (inclusive)
        and the end index (inclusive) that corresponde to the range index
        for the specified page and page size.

    Raises:
        ValueError: When a page and size is not positive integers.

    Example:
        If page = 3 and page size = 10, the function willl return(10, 30)
        for a 0-indexed list.
    """

    # Ensure page and page_size are positive integer
    if (not isinstance(page, int) or
            not isinstance(page_size, int) or
            page <= 0 or
            page_size <= 0):
        raise ValueError("Both page and page_size must be positive integer")

    # Calculate the start and end index
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
