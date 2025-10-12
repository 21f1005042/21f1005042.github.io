import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Tests that a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Tests a simple case with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak_at_beginning():
    """Tests a streak at the beginning of the list."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_single_streak_at_end():
    """Tests a streak at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4

def test_multiple_streaks_longest_first():
    """Tests multiple streaks where the longest streak is first."""
    assert longest_positive_streak([5, 6, 7, 0, 1, 2, -5, 8]) == 3

def test_multiple_streaks_longest_in_middle():
    """Tests multiple streaks where the longest streak is in the middle."""
    assert longest_positive_streak([1, 0, 5, 6, 7, 8, -5, 1, 2]) == 4

def test_multiple_streaks_longest_last():
    """Tests multiple streaks where the longest streak is last."""
    assert longest_positive_streak([1, 2, 0, 1, -5, 5, 6, 7, 8, 9]) == 5

def test_list_with_zeros():
    """Tests that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_list_with_negatives():
    """Tests that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, 2, -3, 4, 5]) == 2

def test_long_list():
    """Tests with a longer list."""
    assert longest_positive_streak([1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5]) == 5