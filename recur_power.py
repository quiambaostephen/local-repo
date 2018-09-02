def recur_power(base, exp):
    '''
        base: int or float.
        exp: int >= 0

        returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    return base * recur_power(base, exp - 1)


recur_power(5, 2)
