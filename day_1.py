"""
Day 1
"""

import numpy as np

data = np.genfromtxt('input/input_1.txt', delimiter=',')

TARGET = 2020

def find_pair(data):
    for i, val in enumerate(data, 1):
        for val_2 in data[i:]:
            if val + val_2 == TARGET:
                print(val * val_2)
                return val, val_2
            

a, b = find_pair(data)

# Part 2

def find_trio(data):
    for i, val in enumerate(data, 1):
        for j, val_2 in enumerate(data[i:], 1):
            for val_3 in data[i+j:]:
                if val + val_2 + val_3 == 2020:
                    print(val * val_2 * val_3)
                    return val, val_2, val_3

a, b, c = find_trio(data)
