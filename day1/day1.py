with open("day1.txt", "r+") as file:
    input = file.read().split("\n")
val_list = []
for row in input:
    numbers = []
    for char in row:
        if char.isnumeric():
            numbers.append(char)
    val_list.append(int(f'{numbers[0]}{numbers[-1]}'))
print("Sum of calib. values", sum(val_list))
