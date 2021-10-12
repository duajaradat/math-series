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
    
    pass

def test_lucas(num):
    if num==1:
        return 1
    if num==0:
        return 2
    if num<0:
        return None
    return test_lucas(num-1)+test_lucas(num-2)         
    pass  
first=0
second=1      
def test_sum_series(num,first,second): 
    if num<0:
        return None
    if num==0:
        return first    