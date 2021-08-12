'''
Day 17
'''
from collections import defaultdict
from operator import add

NUM_CYCLES = 6
INACTIVE = '.'
ACTIVE = '#'
NEIGHBOURS = tuple((x, y, z)
                   for x in (-1, 0, 1)
                   for y in (-1, 0, 1)
                   for z in (-1, 0, 1)
                   if not x == y == z == 0)

with open('input/input_17.txt') as f:
    data = [[i for i in line] for line in f.read().split()]


def initialize_grid(data):
    grid = defaultdict(lambda: INACTIVE)
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == ACTIVE:
                grid[(i, j, 0)] = val
    return grid


def iterate_grid(grid):
    '''
    - If cell is active and 2 or 3 of its neighbours are active it remains
      active, otherwise it becomes inactive.
    - If cell is inactive and 3 of its neighbours are active it becomes
      active.
    '''
    new_grid = defaultdict(lambda: INACTIVE)
    for coord in list(grid.keys()):
        neighbours = find_neighbours(grid, coord)
        if neighbours.count(ACTIVE) in (2, 3):
            new_grid[coord] = ACTIVE
        for neighbour in get_neighbour_coords(coord):
            if find_neighbours(grid, neighbour).count(ACTIVE) == 3:
                new_grid[neighbour] = ACTIVE
    return new_grid


def get_neighbour_coords(coord):
    return [tuple(map(add, coord, delta)) for delta in NEIGHBOURS]


def find_neighbours(grid, coord):
    neighbours = get_neighbour_coords(coord)
    return [grid[coord] for coord in neighbours]


grid = initialize_grid(data)

for _ in range(6):
    grid = iterate_grid(grid)

print(len(grid))

# Part 2
NEIGHBOURS_4D = tuple((x, y, z, w)
                      for x in (-1, 0, 1)
                      for y in (-1, 0, 1)
                      for z in (-1, 0, 1)
                      for w in (-1, 0, 1)
                      if not x == y == z == w == 0)


def initialize_grid_4D(data):
    grid = defaultdict(lambda: INACTIVE)
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == ACTIVE:
                grid[(i, j, 0, 0)] = val
    return grid


def get_neighbour_coords_4D(coord):
    return [tuple(map(add, coord, delta)) for delta in NEIGHBOURS_4D]


def find_neighbours_4D(grid, coord):
    neighbours = get_neighbour_coords_4D(coord)
    return [grid[coord] for coord in neighbours]


def iterate_grid_4D(grid):
    '''
    - If cell is active and 2 or 3 of its neighbours are active it remains
      active, otherwise it becomes inactive.
    - If cell is inactive and 3 of its neighbours are active it becomes
      active.
    '''
    new_grid = defaultdict(lambda: INACTIVE)
    for coord in list(grid.keys()):
        neighbours = find_neighbours_4D(grid, coord)
        if neighbours.count(ACTIVE) in (2, 3):
            new_grid[coord] = ACTIVE
        for neighbour in get_neighbour_coords_4D(coord):
            if find_neighbours_4D(grid, neighbour).count(ACTIVE) == 3:
                new_grid[neighbour] = ACTIVE
    return new_grid


grid = initialize_grid_4D(data)  # Reset the grid


for _ in range(6):
    grid = iterate_grid_4D(grid)

print(len(grid))
