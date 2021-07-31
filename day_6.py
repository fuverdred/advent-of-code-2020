"""
Day 6
"""

with open('input/input_6.txt') as f:
    data = f.read().split('\n\n')

data = [group.split() for group in data]

def group_count(group):
    return len(set(('').join(group)))

print(sum([group_count(group) for group in data]))

# Part 2

def group_count_2(group):
    group = [set(person) for person in group]
    return len(set.intersection(*group))

print(sum([group_count_2(group) for group in data]))
