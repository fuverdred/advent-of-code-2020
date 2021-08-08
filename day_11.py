'''
Day 11
'''

with open("input/input_11.txt") as f:
    data = [[char for char in i.strip('\n')] for i in f.readlines()]

# Modified Conway's game of life
DIRS = tuple((i, j) for j in (-1, 0, 1) for i in (-1, 0, 1)
             if not i == j == 0)


def get_neighbours(data, i, j):
    neighbours = []
    for x, y in DIRS:
        if 0 <= i+x < len(data) and 0 <= j+y < len(data[0]):
            neighbours.append(data[i+x][j+y])
    return neighbours


def iterate_seats(data):
    new_data = [row[:] for row in data]
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            neighbours = get_neighbours(data, i, j)
            if neighbours.count('#') == 0 and val == 'L':
                new_data[i][j] = '#'
            elif neighbours.count('#') > 3 and val == '#':
                new_data[i][j] = 'L'
    return new_data


# old_data = ''
# while old_data != str(data):
#     old_data = str(data)
#     data = iterate_seats(data)

# print(str(data).count('#'))

# Part 2


def get_neighbours(data, i, j):
    neighbours = []
    for x, y in DIRS:
        pos_i, pos_j = i+x, j+y
        while 0 <= pos_i < len(data) and 0 <= pos_j < len(data[0]):
            if data[pos_i][pos_j] in ('L', '#'):
                neighbours.append(data[pos_i][pos_j])
                break
            pos_i += x
            pos_j += y
    return neighbours


def iterate_seats(data):
    new_data = [row[:] for row in data]
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            neighbours = get_neighbours(data, i, j)
            if neighbours.count('#') == 0 and val == 'L':
                new_data[i][j] = '#'
            elif neighbours.count('#') > 4 and val == '#':
                new_data[i][j] = 'L'
    return new_data


old_data = ''
while old_data != str(data):
    old_data = str(data)
    data = iterate_seats(data)

print(str(data).count('#'))
