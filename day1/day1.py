import re

string_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def replace_numbers(row: str):
    for v,k in string_digits.items():
        row = re.sub(v, str(k), row)
    return row
            
with open("day1.txt", "r+") as file:
    input = file.read().split("\n")
val_list = []
for row in input:
    row = replace_numbers(row)
    print(row)
    numbers = []
    for char in row:
        if char.isnumeric():
            numbers.append(char)
    print(numbers)
    if numbers:
	    print(int(f'{numbers[0]}{numbers[-1]}'))
    	val_list.append(int(f'{numbers[0]}{numbers[-1]}'))
print("Sum of calib. values", sum(val_list))
