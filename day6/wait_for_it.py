import re
import numpy as np


def race(tm, dst):
    wins = []
    for i, time in enumerate(tm):
        run = [r*(time-r) for r in range(0, time+1)]
        wins.append(len(list(filter(lambda r: r > dst[i], run))))
    return np.prod(wins)


with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")

times = [int(x) for x in re.findall(r"\d+", data_input[0])]
distances = [int(x) for x in re.findall(r"\d+", data_input[1])]
merged_time = [int(''.join(map(str, times)))]
merged_distance = [int(''.join(map(str, distances)))]

print(f"Part 1: {race(times, distances)}")
print(f"Part 2: {race(merged_time, merged_distance)}")
