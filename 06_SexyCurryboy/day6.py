import re
import math
with open('test.txt', 'r') as f:
    time = re.findall("[0-9]+", f.readline())
    distance = re.findall("[0-9]+", f.readline())
new_time = int("".join(time))
new_distance = int("".join(distance))


def check_for_win(t, d):
    wins = 0
    for j in range(1, t):
        if (t - j) * j > d:
            wins += 1
    return wins


def check_for_win_2(t, d):
    wins = 0
    root = math.sqrt(t**2-(4*d))
    x1 = math.floor((t + root)/2)
    x2 = math.ceil((t - root)/2)
    wins += (x1-x2+1)
    return wins


wins_total = 1
for i in range(len(time)):
    wins_total = check_for_win(int(time[i]), int(distance[i])) * wins_total

print(f"There are {wins_total} wins possible in part 1")
print(f"There are {check_for_win_2(new_time,new_distance)} wins possible in part 2")
