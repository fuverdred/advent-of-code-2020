"""
Day 2
"""

with open("input/input_2.txt") as f:
    data = [password.strip('\n') for password in f.readlines()]
    
# Reconfig data

data = [row.split() for row in data]

total = 0

for lowerupper, letter, password in data:
    lower, upper = lowerupper.split('-')

    letter = letter.strip(':')

    if int(lower) <= password.count(letter) <= int(upper):
        total += 1

print(total)

# Part 2

total = 0

for lowerupper, letter, password in data:
    lower, upper = lowerupper.split('-')

    letter = letter.strip(':')
    
    matches = []
    for index in (int(lower), int(upper)):
        try:
            matches.append(password[index-1]==letter)
        except IndexError:
            matches.append(False)
    if all(matches):
        continue
    if any(matches):
        total += 1

print(total)
