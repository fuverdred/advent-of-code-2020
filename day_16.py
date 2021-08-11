'''
Day 16
'''
from collections import defaultdict


with open('input/input_16.txt') as f:
    ranges, my_ticket, tickets = f.read().split('\n\n')

ranges = ranges.split('\n')


def within_ranges(a, b, c, d):
    return lambda val: (a <= val <= b) or (c <= val <= d)


ranges_dic = {}


for r in ranges:
    name, numbers = r.split(': ')
    numbers = [int(i) for nums in numbers.split(' or ')
               for i in nums.split('-')]
    ranges_dic[name] = within_ranges(*numbers)

tickets = [[int(i) for i in t.split(',')]
           for t in tickets.split('\n')[1:-1]]

total = 0
invalid_tickets = []
for i, ticket in enumerate(tickets):
    for val in ticket:
        if not any([func(val) for func in ranges_dic.values()]):
            total += val
            invalid_tickets.append(i)
            break

print(total)

# Part 2
my_ticket = [int(i) for i in my_ticket.split('\n')[1].split(',')]

valid_tickets = [ticket for i, ticket in enumerate(tickets)
                 if i not in invalid_tickets]


impossible_entries = defaultdict(set)

for ticket in valid_tickets:
    for i, val in enumerate(ticket):
        for name, func in ranges_dic.items():
            if not func(val):
                impossible_entries[name].add(i)

possible_entries = [[name, set(range(20))-vals]
                    for name, vals in impossible_entries.items()]

possible_entries.sort(key=lambda x: x[1], reverse=True)
for i, (_, vals) in enumerate(possible_entries[:-1], 1):
    possible_entries[i-1][1] = vals - possible_entries[i][1]

total = 1
for name, val in possible_entries:
    if 'departure' in name:
        print(name, val)
        total *= my_ticket[val.pop()]

print(total)
