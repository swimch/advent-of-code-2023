import re
with open('input.txt', 'r') as f:
    time = re.findall("[0-9]+", f.readline())
    distance = re.findall("[0-9]+", f.readline())
new_time = int("".join(time))
new_distance = int("".join(distance))


def check_for_win(_time, _distance):
    wins = 0
    for j in range(1, _time):
        if (_time-j) * j > _distance:
            wins += 1
    return wins


wins_total = 1
for i in range(len(time)):
    wins_total = check_for_win(int(time[i]), int(distance[i])) * wins_total

print(f"There are {wins_total} wins possible in part 1")
print(f"There are {check_for_win(new_time,new_distance)} wins possible in part 2")