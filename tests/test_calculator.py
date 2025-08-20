import os
import sys
import pytest

# Ensure root path is in sys.path for direct test execution
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_divide():
    calc = Calculator()
    assert calc.divide(3, 2) == 1.5
    with pytest.raises(ValueError):
        calc.divide(1, 0)
