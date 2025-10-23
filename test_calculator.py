# test_calculator.py
from calculator import add, subtract

def test_add():
    """Test addition"""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    print("✅ Addition test passed!")

def test_subtract():
    """Test subtraction"""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    print("✅ Subtraction test passed!")

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("\n🎉 All tests passed!")
