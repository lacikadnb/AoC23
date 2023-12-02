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

            if result[word.strip()] in results:
                if result[word.strip()] > int(number):
                    result[word.strip()] = int(number)
            else:
                result[word.strip()] = int(number)
        results.append(result)
    game_results[game_id] = results
