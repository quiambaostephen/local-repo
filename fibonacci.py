def fib(x):
    '''
        assumes x an int >= 0

        returns Fibonacci x
    '''
    assert type(x) == int and >= 0
    if x == 1 or x == 0:
        return 1
    else:
        return fib(x - 1) + fib(x + 2)
