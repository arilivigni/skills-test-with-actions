# Additional tests for 100% coverage
import pytest
from calculations import area_of_circle, get_nth_fibonacci

def test_area_of_circle_negative_radius():
    """Test area_of_circle with negative radius raises ValueError."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(-1)

def test_get_nth_fibonacci_negative():
    """Test get_nth_fibonacci with negative n raises ValueError."""
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(-5)
