"""
Day 3
"""

with open("input/input_3.txt") as f:
    data = [line.strip('\n') for line in f.readlines()]

REPEAT_LENGTH = len(data[0])
TREE = '#'
STEP = 3

encounters = [row[(i*3)%REPEAT_LENGTH] for i, row in enumerate(data)]
print(encounters.count(TREE))

# Part 2

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
total = 1
for right, down in slopes:
    encounters = [row[(i*right)%REPEAT_LENGTH]
                  for i, row in enumerate(data[::down])]
    total *= encounters.count(TREE)

print(total)
