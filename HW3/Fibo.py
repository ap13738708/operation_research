number = input('Please input the term n for the Fibonacci sequence: ')


def fibonacci(num):

    if num == 0:
        return 0
    if num <= 2:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)


print 'The Fibonacci sequence = '
for i in range(1, number + 1):
    print fibonacci(i),
