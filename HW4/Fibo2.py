def fibonacci(num):
    if num == 0:
        return 0
    if num <= 2:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)


def fibo2(number):

    result = []
    for i in range(1, number + 1):
        result.append(fibonacci(i))

    return result
