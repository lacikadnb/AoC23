import re

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")

# game data processing
game_results = {}
for row in data_input:
    game_id = int(re.search(r"\d+", row).group())
    game_data = row[row.index(":")+1:]
    results = []
    groups = game_data.split(';')
    for group in groups:
        result = {}
        matches = re.findall(r'(\d+)\s*([a-zA-Z]+)', group)
        for match in matches:
            number, word = match
            result[word.strip()] = int(number)
        results.append(result)
    game_results[game_id] = results

# game runs approximation
run = {"red": 12, "green": 13, "blue": 14}
valid_runs = []
for game in game_results.items():
    current_run = []
    for game_set in game[1]:
        for color in game_set:
            if game_set[color] <= run[color]:
                current_run.append(1)
            else:
                current_run.append(0)
    if all(current_run):
        valid_runs.append(game[0])
print(sum(valid_runs))
