def recur_fact(n):
    '''
        assumes that n is an int > 0

        returns n!
    '''
    if n == 1:
        return n
    else:
        return n * recur_fact(n - 1)


recur_fact(5)
