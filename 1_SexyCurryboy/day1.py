import re
input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line[:-1])

### Part 1 ###
digits = []
values = []
for line in input:
    for char in line:
        if char.isdigit():
            digits.append(char)
    values.append(int(digits[0]+digits[-1]))
    digits = []
print(sum(values))