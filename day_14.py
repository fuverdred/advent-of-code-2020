'''
Day 14
'''
from collections import defaultdict


with open('input/input_14.txt') as f:
    data = f.read().split('mask = ')[1:]

chunks = [chunk.split('\n')[:-1] for chunk in data]

BITS = 36


def apply_mask(val, mask):
    val = bin(val)[2:].rjust(BITS, '0')
    return int(''.join([i if j == 'X' else j for i, j in zip(val, mask)]), 2)


def split_op(op):
    address, val = op.split(' = ')
    address = ''.join([i for i in address if i.isdigit()])
    return int(address), int(val)


mem = defaultdict(int)

for chunk in chunks:
    mask = chunk[0]
    for op in chunk[1:]:
        address, val = split_op(op)
        val = apply_mask(val, mask)
        mem[address] = val

print(sum(mem.values()))


def bin_apply_mask(val, mask):
    mask_1 = int(''.join([i if i == '1' else '0' for i in mask]), 2)
    val_1 = val | mask_1
    mask_0 = int(''.join([i if i == '0' else '1' for i in mask]), 2)
    val_2 = val_1 & mask_0
    return val_2


# Part 2
mem = defaultdict(int)


def recursive_mask(mask, addr, new=''):
    if not mask:
        addr = int(new, 2)
        mem[addr] = val
        return
    if mask[0] == '1':
        recursive_mask(mask[1:], addr[1:], new + '1')
    elif mask[0] == '0':
        recursive_mask(mask[1:], addr[1:], new + addr[0])
    elif mask[0] == 'X':
        recursive_mask(mask[1:], addr[1:], new + '1')
        recursive_mask(mask[1:], addr[1:], new + '0')
    return


for chunk in chunks:
    mask = chunk[0]
    for op in chunk[1:]:
        addr, val = split_op(op)
        addr = bin(addr)[2:].rjust(BITS, '0')
        recursive_mask(mask, addr)

print(sum(mem.values()))
