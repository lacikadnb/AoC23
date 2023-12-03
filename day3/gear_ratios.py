import re

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")

valid_gears = []
for i, row in enumerate(data_input):
    numbers = re.findall(r"\d+", row)
    length = len(row)
    for number in numbers:
        indexes = [[x.start(0), x.end(0)] for x in re.finditer(number, row)]
        for j in range(int(indexes[0][0])-1, int(indexes[0][1])+1):
            if i > 0 and j < length:
                if data_input[i][j] != "." and not data_input[i][j].isnumeric():
                    valid_gears.append(int(number))
                    break
            if i > 0 and j < length:
                if data_input[i-1][j] != "." and not data_input[i-1][j].isnumeric():
                    valid_gears.append(int(number))
                    break
            if i < length - 1 and j < length:
                if data_input[i + 1][j] != "." and not data_input[i + 1][j].isnumeric():
                    valid_gears.append(int(number))
                    break
print(f'Sum of all of the part numbers in the engine schematic is {sum(valid_gears)}')
