# fibonacci
num=int(input())

def test_fibonacci(num): 
    if num==1:
        return 1
    if num==0:
        return 0
    if num<0:
        return None
    return test_fibonacci(num-1)+test_fibonacci(num-2)           
    """
    should return the nth value in the fibonacci series
    """
    pass

def test_lucas(num):
    if num==1:
        return 1
    if num==0:
        return 2
    pass        