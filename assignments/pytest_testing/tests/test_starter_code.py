from assignments.pytest_testing.starter_code import add_numbers, is_palindrome, filter_positive_numbers


def test_add_numbers():
    assert add_numbers(3, 5) == 8
    assert add_numbers(-1, 1) == 0


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("Hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True


def test_filter_positive_numbers():
    assert filter_positive_numbers([3, -1, 0, 5]) == [3, 5]
    assert filter_positive_numbers([-5, -2]) == []
