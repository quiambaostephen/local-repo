def iter_mul(a, b):
    result = 0

    while b > 0:
        result += a
        b -= 1
    return result


a = iter_mul(5, 2)
print(a)
