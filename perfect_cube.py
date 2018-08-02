# A program that would check if a number is a perfect cube

x = int(input('Enter an integer: '))

for ans in range(0, abs(x) + 1):
    if ans1 ** 3 == abs(x):
        break
if ans1 ** 3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans1 = -ans1
    print('Cube root of ' + str(x) + ' is ' + str(ans))
