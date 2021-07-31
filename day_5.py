"""
Day 5
"""

with open('input/input_5.txt') as f:
    data = [row.strip('\n') for row in f.readlines()]

data = [[row[:-3], row[-3:]] for row in data]

def binarise_row(row):
    convert = {'B': '1',
               'F': '0'}
    return int(''.join([convert[c] for c in row]), 2)

def binarise_column(col):
    convert = {'R': '1',
               'L': '0'}
    return int(''.join([convert[c] for c in col]), 2)

def seat_ID(ticket):
    return binarise_row(ticket[0]) * 8 + binarise_column(ticket[1])

seat_ids = [seat_ID(ticket) for ticket in data]
highest = max(seat_ids)

print(highest)

lowest = min(seat_ids)
missing = set(range(lowest, highest+1)).difference(set(seat_ids))
print(missing)
