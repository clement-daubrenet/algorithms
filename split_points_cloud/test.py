from solution import is_exact_split
import pytest


@pytest.mark.parametrize('points, x_split', 
        [([(1,3), (3,3)], 2), ([(2,6), (2, 15), (3, 4), (6, 6), (6, 15), (5,4)], 4)])
def test_is_exact_split(points, x_split):
    assert is_exact_split(points, x_split) is True

def test_is_exact_split_false():
    assert is_exact_split([(3,2), (1,2), (3,8)], 3) is False
