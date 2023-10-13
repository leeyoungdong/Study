def factorial_iterative(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

def factorial_recursvie(n):
    if n <=1:
        return 1
    # n! = n * (n-1)!
    return n * factorial_recursvie(n-1)

print('반복', factorial_iterative(5))
print('재귀', factorial_recursvie(5))