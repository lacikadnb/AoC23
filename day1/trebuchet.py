import re

string_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")
val_list = []
for row in data_input:
    numbers = {}
    # ------------------------------------------ Part 2 start --------------------------------------------------- #
    # Scan for written numbers
    for k, v in string_digits.items():
        if re.search(k, row):
            indexes = [x.start(0) for x in re.finditer(k, row)]
            for i in indexes:
                numbers[i] = str(v)
    # ------------------------------------------ Part 2 end ---------------------------------------------------- #
    # Scan for arabic numbers
    for i, char in enumerate(row):
        if char.isnumeric():
            numbers[i] = char
    sorted_numbers = sorted(numbers.items())
    val_list.append(int(f'{sorted_numbers[0][1]}{sorted_numbers[-1][1]}'))
print("Sum of calib. values", sum(val_list))
