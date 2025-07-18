import pytest

from recipes import sample_function
def test_recipes_has_sample_function():
    assert sample_function() is None  # no return value
