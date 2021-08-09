'''
Day 12
'''
from math import sin, cos
import numpy as np


with open('input/input_12.txt') as f:
    data = f.read().split()

DIRS = ['N', 'E', 'S', 'W']


def rotate_right(current_direction, angle):
    return DIRS[(DIRS.index(current_direction) + angle // 90) % 4]


def rotate_left(current_direction, angle):
    return DIRS[(DIRS.index(current_direction) - angle // 90) % 4]


action_dic = {'N': lambda i, j, val: (i+val, j),
              'S': lambda i, j, val: (i-val, j),
              'E': lambda i, j, val: (i, j+val),
              'W': lambda i, j, val: (i, j-val)}

rotate_dic = {'R': rotate_right,
              'L': rotate_left}

direction = 'E'
location = (0, 0)
for action in data:
    instr, val = action[:1], int(action[1:])
    if instr in rotate_dic.keys():
        direction = rotate_dic[instr](direction, val)
        continue
    elif instr == 'F':
        instr = direction
    location = action_dic[instr](*location, val)

print(sum(map(abs, location)))

# Part 2


def deg_to_rad(angle):
    return (angle/180) * np.pi


def rotation_matrix(angle):
    angle = deg_to_rad(angle)
    return np.array([[cos(angle), -sin(angle)],
                     [sin(angle), cos(angle)]]).astype(int)


def rotate(ship, waypoint, angle):
    relative_coord = waypoint - ship
    relative_coord = np.matmul(rotation_matrix(angle),
                               relative_coord)
    return (ship + relative_coord)


ship = np.array((0, 0))
waypoint = np.array((1, 10))


for instruction in data:
    instr, val = instruction[0], int(instruction[1:])
    if instr in ('R', 'L'):
        if instr == 'L':
            val *= -1
        waypoint = rotate(ship, waypoint, val)
    elif instr == 'F':
        move = val * (waypoint - ship)
        ship += move
        waypoint += move
    else:
        waypoint = np.array(action_dic[instr](*waypoint, val))


print(sum(map(abs, ship)))
