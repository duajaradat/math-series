from math_series.series import test_fibonacci

# fibonacci

def test_fibonacci_return_first_number():
    actual = test_fibonacci(0)
    expected=0
    assert actual == expected

def test_fibonacci_return_second_number():
    actual = test_fibonacci(1)
    expected=1
    assert actual == expected

def test_fibonacci_return_LessThanZero_number():
    number=-3
    actual = None
    expected=None
    assert actual == expected    