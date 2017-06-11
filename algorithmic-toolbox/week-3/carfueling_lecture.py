def min_refills(x, capacity):
    """
    Find the minimum no. of refills needed to reach the destination.

    :param x: array of stops available including start and stop
    :param capacity: units, a car can travel with full capacity
    """
    current_capacity = capacity - x[1]
    print(current_capacity)
    stops_taken = []
    stops_skipped = []
    for index in range(1, len(x) - 1):
        if x[index] - x[index - 1] <= current_capacity and x[index + 1] - x[index] <= current_capacity:
            stops_skipped.append(x[index])
            current_capacity = current_capacity - (x[index] - x[index - 1])
        else:
            stops_taken.append(x[index])
            current_capacity = capacity
    print(stops_taken)
    print(stops_skipped)


min_refills([0, 1, 2, 3, 4, 7, 10], 3)
