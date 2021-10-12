from math_series.series import test_fibonacci
from math_series.series import test_lucas
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

def test_fibonacci_return_7_number():
    number=7
    actual = 13
    expected=13
    assert actual == expected  

def test_fibonacci_enter_number_bigger_than_1__number():
    num=8
    actual = test_fibonacci(num-1)+test_fibonacci(num-2)
    expected=21
    assert actual == expected 

    # lucas
def test_lucas_enter_one_number():
    actual = test_lucas(1)
    expected=1
    assert actual == expected

def test_lucas_enter_zero_number():
    actual = test_lucas(0)
    expected=2
    assert actual == expected  

def test_lucas_enter_number_less_than_zeron():
    actual = test_lucas(-1)
    expected=None
    assert actual == expected     