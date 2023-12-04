import re

total_cards = 0
cards = [([], [])]

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")


def scratch_card(n_card):
    global total_cards
    wining_cards = 0
    var_card = cards[n_card]
    for number in var_card[0]:
        if number in var_card[1]:
            total_cards += 1
            wining_cards += 1
    for i in range(1, wining_cards+1):
        if n_card+i < len(cards):
            scratch_card(n_card+i)


for row in data_input:
    card_id = int(re.search(r"\d+", row).group())
    group = row[row.index(":") + 1:].split('|')
    cards.append(([int(x) for x in group[0].rstrip().lstrip().replace(" ", ",").split(",") if x],
                 [int(x) for x in group[1].rstrip().lstrip().replace(" ", ",").split(",") if x]))
for j in range(1, len(cards)):
    total_cards += 1
    scratch_card(j)

print(total_cards)
