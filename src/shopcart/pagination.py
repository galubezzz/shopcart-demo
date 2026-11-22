"""Pagination for order listings (pages are 1-based)."""

import math


def total_pages(n_items: int, per_page: int) -> int:
    return max(1, math.ceil(n_items / per_page))


def get_page(items: list, page: int, per_page: int = 10) -> list:
    pages = total_pages(len(items), per_page)
    if page < 1 or page >= pages:
        raise IndexError(f"page {page} out of range (1..{pages})")
    start = (page - 1) * per_page
    return items[start : start + per_page]
