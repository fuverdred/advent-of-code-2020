"""
Day 8
"""

visited_indices = []
accumulator = 0
index = 0

with open('input/input_8.txt') as f:
    data = [op.strip('\n') for op in f.readlines()]

def acc(val):
    return 1, val # return 1 to increment the index

def jmp(val):
    return val, 0

def nop(val):
    return 1, 0

ops = {'acc': acc,
       'jmp': jmp,
       'nop': nop}

def run_row(row):
    op, val = row.split()
    return ops[op](int(val))

while 1:
    if index in visited_indices:
        break
    visited_indices.append(index)
    i, a = run_row(data[index])
    index += i
    accumulator += a

print(accumulator)

# Part 2
test="""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
test = test.split('\n')


def test_prog(data):
    index = 0
    accumulator = 0
    visited_indices = []
    while 1:
        if index in visited_indices:
            return False
        if index == len(data):
            return accumulator
        if index > len(data):
            return False
        visited_indices.append(index)
        i, a = run_row(data[index])
        index += i
        accumulator += a

for i, row in enumerate(data):
    if 'jmp' in row:
        new = 'nop ' + row.split(' ')[1]
        result = test_prog([*data[:i], new, *data[i+1:]])
        if result != False:
            print(result)
            break
