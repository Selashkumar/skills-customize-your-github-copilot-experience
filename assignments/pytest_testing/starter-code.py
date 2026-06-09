from typing import List


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def is_palindrome(text: str) -> bool:
    """Return True if the text is the same forwards and backwards."""
    normalized = text.replace(" ", "").lower()
    return normalized == normalized[::-1]


def filter_positive_numbers(numbers: List[int]) -> List[int]:
    """Return only the positive numbers from the list."""
    return [value for value in numbers if value > 0]
