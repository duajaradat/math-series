from math_series.series import test_fibonacci
from math_series.series import test_lucas
from math_series.series import test_sum_series
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
def test_lucas_enter_number_more_than_zero():
    actual = test_lucas(5)
    expected=11
    assert actual == expected       
    # sum_series
def test_sum_series_enter_number_less_than_zero():
    actual = test_lucas(-9)
    expected=None
    assert actual == expected      
def test_sum_series_enter_number_zero():
    actual = test_sum_series(0,0,1)
    expected=0
    assert actual == expected 
def test_sum_series_enter_number_one():
    actual = test_sum_series(1,0,1)
    expected=1
    assert actual == expected      
# def test_sum_series_enter_numbermore_than_zero():
#     actual = test_sum_series(7,0,1)
#     expected=42
#     assert actual == expected          