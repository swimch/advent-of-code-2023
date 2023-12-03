# schauen isdigit, wenn ja in cache und rundherum checken, dann rechts weiter checken und an cache anfügen
input_data = []
with open('input.txt', 'r') as f:
    for line in f:
        input_data.append(line[:-1])


# check if surrounding chars are special chars
def special_chars(row, column, rows, columns):
    # staying in range
    if row == 0:
        over = 0
        under = 2
    elif row == rows - 1:
        over = -1
        under = 1
    else:
        over = -1
        under = 2

    if column == 0:
        left = 0
        right = 2
    elif column == columns - 1:
        left = -1
        right = 1
    else:
        left = -1
        right = 2

    check_result = False
    for y in range(over, under):
        for x in range(left, right):
            if not input_data[row + y][column + x].isdigit() and not input_data[row + y][column + x] == ".":
                check_result = True
            if input_data[row + y][column + x] == "*":


    return check_result


cache = ""
is_part = False
parts = []


# loop through input
for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        # if digit -> add to cache and check surroundings
        if input_data[i][j].isdigit():
            cache += input_data[i][j]
            if not is_part:
                is_part = special_chars(i, j, len(input_data), len(input_data[i]))
        # if not a digit but is_part == True -> part ended here and add cache to parts
        elif is_part:
            parts.append(int(cache))
            cache = ""
            is_part = False
        # wasn't a part and not a digit -> empty cache
        else:
            cache = ""

print(sum(parts))
