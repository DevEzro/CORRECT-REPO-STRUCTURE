import pytest
from app import suma, resta, multiplicacion, division

def test_suma():
    assert suma() == 5  # 3 + 2 = 5

def test_resta():
    assert resta() == 1  # 3 - 2 = 1

def test_multiplicacion():
    assert multiplicacion() == 6  # 3 * 2 = 6

def test_division():
    assert division() == 1.5  # 3 / 2 = 1.5

if __name__ == "__main__":
    pytest.main()