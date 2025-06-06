# tests/test_triangle.py

import pytest
from triangle import area_triangle

def test_area_base_5_height_7():
    """
    Validate the result when the base is 5 and the height is 7.
    Expected area = (5 * 7) / 2 = 17.5
    """
    result = area_triangle(5, 7)
    assert result == 17.5

@pytest.mark.parametrize(
    "b, h",
    [
        (-1, 5),   # negative base
        (5, -2),   # negative height
        (-3, -4),  # both negative
    ],
)
def test_negative_values_not_accepted(b, h):
    """
    Validate that negative values for base and/or height raise ValueError.
    """
    with pytest.raises(ValueError):
        _ = area_triangle(b, h)

def test_base_not_zero():
    """
    Validate that base = 0 raises ValueError.
    (Height could be a positive number, e.g. 4; but base=0 is invalid.)
    """
    with pytest.raises(ValueError):
        _ = area_triangle(0, 4)

def test_height_not_zero():
    """
    (Optional) Validate that height = 0 also raises ValueError. 
    We said height <= 0 is invalid, so this covers that too.
    """
    with pytest.raises(ValueError):
        _ = area_triangle(5, 0)
