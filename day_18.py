'''
Day 18
'''
import re
from operator import add, mul

OPS = {'+': add,
       '*': mul}

with open('input/input_18.txt') as f:
    data = [line.strip('\n') for line in f.readlines()]


def evaluate(string):
    string = ''.join([i for i in string if i != ' '])  # Remove spaces
    vals = [int(i) for i in re.split('\\+|\\*', string) if i]
    ops = [OPS[op] for op in re.split('[0-9]', string) if op]
    total = vals[0]
    for val, op in zip(vals[1:], ops):
        total = op(total, val)
    return total


def recursive(vals, string="", depth=0):
    if not vals:
        return vals, string
    if vals[0] == '(':
        vals, substring = recursive(vals[1:], "", depth+1)
        string += substring
        if not vals:
            return vals, string
    if vals[0] == ')':
        return vals[1:], str(new_evaluate(string))
    vals, string = recursive(vals[1:], string+vals[0], depth+1)
    if depth == 0:
        return new_evaluate(string)
    return vals, string


# Part 2


def new_evaluate(string):
    string = ''.join([i for i in string if i != ' '])  # Remove spaces
    string = [str(eval(x)) if '+' in x else x for x in string.split('*')]
    return eval('*'.join(string))


print(sum([recursive(line) for line in data]))
