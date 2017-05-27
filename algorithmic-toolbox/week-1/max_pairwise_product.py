# Uses python3

n = int(input())
numbers = [int(x) for x in input().split()]
assert (len(numbers) == n)

a = 0
b = 0

for number in numbers:
    if a < number:
        b = a
        a = number
    elif b < number:
        b = number

print(a*b)
