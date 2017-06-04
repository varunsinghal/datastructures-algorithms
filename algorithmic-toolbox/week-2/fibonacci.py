# Uses python3
def calc_fib(number):
    if number == 0:
        return 0
    first = 0
    second = 1
    for i in range(2, number + 1):
        first, second = second, first + second
    return second


n = int(input())
print(calc_fib(n))
