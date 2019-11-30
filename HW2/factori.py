num = input('Please input N for the Factorial: ')
result = num
while True:
    if result == 0:
        result = 1
        break

    num = num - 1
    if num == 0:
        break
    result = result * num

print 'The Factorial = {}'.format(result)
