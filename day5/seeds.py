def extend_numbers(original_list):
    result = []
    size = int(original_list[2])
    for num_str in original_list[:-1]:
        num = int(num_str)
        result.extend(range(num, num + size))
    return result


with open("example.txt", "r+") as file:
    data_input = file.read().split("\n")

seeds = data_input[0][data_input[0].index(":")+1:].lstrip().replace(" ", ",").split(",")
data_input.pop(0)
data_input.pop(0)
maps_list = []
current_map = None

for item in data_input:
    if item.endswith('map:'):
        item = item.replace("-to", "")
        if current_map:
            maps_list.append(current_map)
        current_map = [item[:-5].split('-')]
    elif item:
        current_map.append(item.split())

# Append the last map if any
if current_map:
    maps_list.append(current_map)

for field_map in maps_list:
    for ranges in field_map[1:]:
        res = extend_numbers(ranges)
        print(res)

