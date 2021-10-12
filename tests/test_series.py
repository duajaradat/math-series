from math_series.series import test_fibonacci

# fibonacci

def test_fibonacci_return_first_number():
    actual = test_fibonacci(0)
    expected=0
    assert actual == expected