'''
Day 13
'''

from functools import reduce

with open('input/input_13.txt') as f:
    data = f.read().split()

earliest_departure_time = int(data[0])

buses = [int(i) for i in data[1].split(',') if i != 'x']


def wait_time(bus):
    return bus - (earliest_departure_time % bus)


wait_times = list(map(wait_time, buses))
print(min(wait_times) * buses[wait_times.index(min(wait_times))])

# part 2
start_time = 0
bus_times = [(int(val), i) for i, val in enumerate(data[1].split(','))
             if val != 'x']

n = [7, 13, 59, 31, 19]
i = [0, 1, 4, 6, 7]


def chinese_remainder(n, a):
    total = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total += a_i * mul_inv(p, n_i) * p
    return total % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 > 0:
        x1 += b0
    return x1


offsets = [int(b)-i for i, b in enumerate(data[1].split(','))
           if b != 'x']
print(f'Part 2: {chinese_remainder(buses, offsets)}')
