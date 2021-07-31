"""
Day 7
"""

test = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

test = test.split('\n')
test = [row.strip('.') for row in test]

TARGET = "shiny gold"

with open('input/input_7.txt') as f:
    data = [row.strip('\n').strip('.') for row in f.readlines()]

def clean_data(row):
    root, leaves = row.split(" bags contain ")
    leaves = leaves.split(', ')
    if leaves[0] == "no other bags":
        return root, []
    return root, [' '.join(bag.split(' ')[1:3]) for bag in leaves]

data1 = dict([clean_data(row) for row in data])

def recursive_search(bag):
    if bag == TARGET:
        return 1
    for child_bag in data1[bag]:
        if recursive_search(child_bag):
            return 1
    return 0

count = sum([recursive_search(bag) for bag in data1.keys() if bag != TARGET])
print(count)

# Part 2

test2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''

test2 = test2.split('\n')
test2 = [row.strip('.') for row in test2]

def clean_data_2(row):
    root, leaves = row.split(" bags contain ")
    leaves = leaves.split(', ')
    if leaves[0] == "no other bags":
        return root, []
    return root, [[' '.join(bag.split(' ')[1:3]), int(bag.split(' ')[0])] for bag in leaves]

def recursive_2(bag):
    total = 1
    for child_bag, count in data[bag]:
        total += count * recursive_2(child_bag)
    return total

data = dict([clean_data_2(row) for row in data])

print(recursive_2(TARGET)-1)
