'''
Day 15
'''

from collections import defaultdict

data = [6, 19, 0, 5, 7, 13, 1]

cache = defaultdict(lambda: -1)

for i, val in enumerate(data[:-1], 1):
    cache[val] = i

last_val = data[-1]
for i in range(len(data), 30000000):
    if cache[last_val] == -1:
        cache[last_val] = i
        last_val = 0
    else:
        diff = i - cache[last_val]
        cache[last_val] = i
        last_val = diff


print(last_val)
