"""
Day 9
"""

with open('input/input_9.txt') as f:
    data = [int(x.strip('\n')) for x in f.readlines()]

    
LENGTH = 25

def can_sum(value, lst):
    for i, pair_1 in enumerate(lst[:-1], 1):
        for pair_2 in lst[i:]:
            if pair_1 + pair_2 == value:
                return True
    return False

for i, value in enumerate(data[LENGTH:]):
    if not can_sum(value, data[i:i+LENGTH]):
        print(value)
        break

# Part 2

def find_contiguous(index):
    i, total = 0, 0
    while 1:
        total += data[index+i]
        if total == value and i>0:
            return data[index: index+i+1]
        if total > value:
            return
        i += 1

for i, _ in enumerate(data):
    run = find_contiguous(i)
    if run:
        print(max(run) + min(run))
