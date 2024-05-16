#!/usr/bin/env python3
"""Module to retrieve start and end indexes corresponding to the range
of indexes to return in a list for particular pagination parameters."""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing start and end indexes for pagination."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
