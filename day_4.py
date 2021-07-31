"""
Day 4
"""

from collections import defaultdict

passport = defaultdict(list)
passport_keys = ('byr',
                 'iyr',
                 'eyr',
                 'hgt',
                 'hcl',
                 'ecl',
                 'pid')

with open('input/input_4.txt') as f:
    data = f.read().split('\n\n')

data = [row.split() for row in data]
data = [[entry.split(':') for entry in row] for row in data]
# Convert to a list of dics
data = [{key: value for key, value in row} for row in data]

def validate(passport):
    for key in passport_keys:
        try:
            _ = passport[key]
        except KeyError:
            return False
    return True

print(sum([1 if validate(passport) else 0 for passport in data]))

# Part 2

def byr_valid(val):
    val = int(val)
    if 1920 <= val <= 2002:
        return True
    return False

def iyr_valid(val):
    val = int(val)
    if 2010 <= val <= 2020:
        return True
    return False

def eyr_valid(val):
    val = int(val)
    if 2020<= val <= 2030:
        return True
    return False

def hgt_valid(val):
    unit = val[-2:]
    try:
        val = int(val[:-2])
        if unit == "cm":
            if 150 <= val <= 193:
                return True
        if unit == "in":
            if 59 <= val <= 76:
                return True
    except ValueError:
        return False
    return False

def hcl_valid(val):
    if val[0] != '#':
        return False
    if len(val[1:]) != 6:
        return False
    try:
        val = int(val[1:], 16)
        if 0 <= val <= 0xFFFFFF:
            return True
    except ValueError:
        return False
    return False

def ecl_valid(val):
    if val in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return True
    return False

def pid_valid(val):
    if len(val) != 9:
        return False
    try:
        val = int(val)
        if 0 <= val <= 999999999:
            return True
    except:
        return False
    return False

valid_funcs = (byr_valid,
               iyr_valid,
               eyr_valid,
               hgt_valid,
               hcl_valid,
               ecl_valid,
               pid_valid)

valid_dic = {key: func for key, func in zip(passport_keys, valid_funcs)}

from collections import defaultdict

fails = defaultdict(int)

def validate_2(passport):
    for key in passport_keys:
        try:
            valid = valid_dic[key](passport[key])
            if not valid:
                fails[key] += 1
                return False
        except KeyError:
            return False
    return True

print(sum([1 if validate_2(passport) else 0 for passport in data]))
