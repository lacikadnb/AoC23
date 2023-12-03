import re

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")

valid_gears = []
for i, row in enumerate(data_input):
    matches = re.finditer(r"\d+", row)
    length = len(row)
    for match in matches:
        start_col_index = match.start()
        end_col_index = match.end()
        number = match.group()
        index = [start_col_index, end_col_index]
        for j in range(int(index[0])-1, int(index[1])+1):
            # Check number in actual row
            if i > 0 and j < length:
                if data_input[i][j] != "." and not data_input[i][j].isnumeric():
                    valid_gears.append(int(number))
                    break
            # Check number in upper row
            if i > 0 and j < length:
                if data_input[i-1][j] != "." and not data_input[i-1][j].isnumeric():
                    valid_gears.append(int(number))
                    break
            # Check number in actual lower row
            if i < length - 1 and j < length:
                if data_input[i+1][j] != "." and not data_input[i+1][j].isnumeric():
                    valid_gears.append(int(number))
                    break
print(f'Sum of all of the part numbers in the engine schematic is {sum(valid_gears)}')
