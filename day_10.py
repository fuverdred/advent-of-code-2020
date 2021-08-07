"""
Day 10
"""

import numpy as np

data = list(np.genfromtxt('input/input_10.txt', delimiter='\n', dtype=int))
data.sort()

data.insert(0, 0)
data.append(data[-1]+3)
diffs = list(np.diff(data))

print(diffs.count(1) * (diffs.count(3) + 1))

# Part 2

# 11 => (11, 2) 2
# 111 => (111, 21, 12, 3) 4
# 1111 => (1111, 211, 121, 112, 22, 31, 13) 6


comb_dic = {2: 2,
            3: 4,
            4: 7}

diffs = ''.join([str(i) for i in diffs]).split('3')
diffs = [i for i in diffs if len(i) > 1]

total = 1
for ones in diffs:
    total *= comb_dic[len(ones)]
print(total)
