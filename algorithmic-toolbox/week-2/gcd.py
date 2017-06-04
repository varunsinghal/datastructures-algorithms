from time import time


def naive_gcd(a, b):
    best = 0
    for i in range(1, a + b):
        if a % i == 0 and b % i == 0:
            best = i
    return best


def euclid_gcd(a, b):
    if b == 0:
        return a
    return euclid_gcd(b, a % b)


input_cases = [(357, 234), (312312, 1242344), (100, 150)]
for item in input_cases:
    start = time()
    print("naive gcd for %r : %d" % (item, naive_gcd(item[0], item[1])))
    end = time()
    print("Time taken by naive approach: %f seconds" % (end - start))
    start = time()
    print("Euclid gcd for %r : %d" % (item, euclid_gcd(item[0], item[1])))
    end = time()
    print("Time taken by Euclid approach: %f seconds" % (end - start))
    print()
