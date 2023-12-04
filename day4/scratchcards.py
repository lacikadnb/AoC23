import re

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")

all_points = 0
for row in data_input:
    card_id = int(re.search(r"\d+", row).group())
    group = row[row.index(":")+1:].split('|')
    actual_numbers = [int(x) for x in group[0].rstrip().lstrip().replace(" ", ",").split(",") if x]
    wining_numbers = [int(x) for x in group[1].rstrip().lstrip().replace(" ", ",").split(",") if x]
    card_points = 0
    i = 0
    for number in actual_numbers:
        if number in wining_numbers:
            i += 1
            if i == 1:
                card_points += 1
            else:
                card_points *= 2
    all_points += card_points
print(f'Points worth in total: {all_points}')
