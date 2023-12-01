import re

string_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open("input.txt", "r+") as file:
    data_input = file.read().split("\n")
val_list = []
for row in data_input:
    numbers = {}
    # Scan for written numbers
    for k, v in string_digits.items():
        if re.search(k, row):
            indexes = [m.start(0) for m in re.finditer(k, row)]
            for i in indexes:
                numbers[i] = str(v)
    # Scan for arabic numbers
    for num, char in enumerate(row):
        if char.isnumeric():
            numbers[num] = char
    sorted_numbers = dict(sorted(numbers.items())) # NOQA
    numbers = list(sorted_numbers.values())
    val_list.append(int(f'{numbers[0]}{numbers[-1]}'))
print("Sum of calib. values", sum(val_list))
