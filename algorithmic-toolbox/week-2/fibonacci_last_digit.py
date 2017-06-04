# Uses python3
import sys


def get_fibonacci_last_digit_naive(number):
    if number == 0:
        return 0
    first = 0
    second = 1
    for i in range(2, number + 1):
        first, second = second, (first + second) % 10
    return second


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
