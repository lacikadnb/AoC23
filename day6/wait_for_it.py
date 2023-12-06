import re
import numpy as np

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")
    merged_input = [re.sub(" ", "", row) for row in data_input]

times = [int(x) for x in re.findall(r"\d+", data_input[0])]
distances = [int(x) for x in re.findall(r"\d+", data_input[1])]
merged_time = [int(x) for x in re.findall(r"\d+", merged_input[0])]
merged_distance = [int(x) for x in re.findall(r"\d+", merged_input[1])]


def race(tm, dst):
    results = []
    for i, time in enumerate(tm):
        run = []
        for t in range(0, time+1):
            speed = t*1
            duration = time-t
            result = speed*duration
            run.append(result)
        results.append(run)

    wins = []
    for i, run in enumerate(results):
        d = dst[i]
        win = 0
        for r in run:
            if r > d:
                win += 1
        wins.append(win)
    return np.prod(wins)


print(f"Part 1: {race(times, distances)}")
print(f"Part 2: {race(merged_time, merged_distance)}")
