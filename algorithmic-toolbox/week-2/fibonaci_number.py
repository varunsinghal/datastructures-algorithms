import time


def fib_recurs(n: int) -> int:
    if n <= 1:
        return 1
    return fib_recurs(n - 1) + fib_recurs(n - 2)


def fib_algorithm(n: int) -> int:
    fib_list = [1, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n]


input_numbers = [35, 40, 45]

for number in input_numbers:
    start_time = time.time()
    print("Fibonaci number at %d - %d " % (number, fib_recurs(number)))
    end_time = time.time()
    print("Time taken by naive approach: %f seconds" % (end_time - start_time))

    start_time = time.time()
    print("Fibonaci number at %d - %d " % (number, fib_algorithm(number)))
    end_time = time.time()
    print("Time taken by efficient approach: %f seconds" % (end_time - start_time))
