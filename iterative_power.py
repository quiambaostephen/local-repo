def iterativePower(x, p):
    result = 1

    for turn in range(p):
        print('Iteration: ' + str(turn) + ' result: ' + str(result))
        result *= x
    return result


a = iterativePower(3, 5)
print(a)
