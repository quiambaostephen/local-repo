def iter_fact(n):
    '''
        assumes that n is an int > 0

        returns n!
    '''
    result = 1

    while n > 1:
        result *= n
        n -= 1
    return result


iter_fact(5)
