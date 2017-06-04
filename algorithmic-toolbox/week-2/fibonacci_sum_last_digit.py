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


def fibonacci_sum_naive(number):
    lower_number = number % get_pisano_period(10)
    sum = 0
    for i in range(lower_number + 1):
        sum += get_fibonacci(i)
    return sum % 10


if __name__ == '__main__':
    input = input()  # sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
