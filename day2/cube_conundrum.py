import re
import numpy as np

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")

# game data processing
game_results = {}
for row in data_input:
    game_id = int(re.search(r"\d+", row).group())
    groups = row[row.index(":")+1:].split(';')
    row_buffer = {"red": 0, "green": 0, "blue": 0}
    for group in groups:
        matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', group)
        for match in matches:
            number, word = match
            if row_buffer[word.strip()] < int(number):
                row_buffer[word.strip()] = int(number)
    game_results[game_id] = row_buffer

# game runs approximation
limit = {"red": 12, "green": 13, "blue": 14}
valid_runs = []
for game in game_results.items():
    if game[1]["red"] <= limit["red"] and game[1]["green"] <= limit["green"] and game[1]["blue"] <= limit["blue"]:
        valid_runs.append(game[0])
print(f'Sum of the IDs of valid games is: {sum(valid_runs)}')

# min cubes for successful run
powers = []
for run in list(game_results.values()):
    powers.append(np.prod(list(run.values())))
print(f'Sum of the power of valid sets is: {sum(powers)}')
