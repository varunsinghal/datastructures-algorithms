# Uses python3
import sys


def get_fibonacci(number):
    if number == 0:
        return 0
    first = 0
    second = 1
    for i in range(2, number + 1):
        first, second = second, first + second
    return second


def get_pisano_period(number):
    a = 0
    b = 1
    c = a + b
    for i in range(number * number):
        c = (a + b) % number
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1


def get_fibonacci_huge_naive(n, m):
    tiny = n % get_pisano_period(m)
    return get_fibonacci(tiny) % m


if __name__ == '__main__':
    input = input()  # sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
