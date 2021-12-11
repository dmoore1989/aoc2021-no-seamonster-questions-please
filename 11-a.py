f = open("11in.txt", "r")
output = f.readlines()
map = []
nearby = [
    (1,0),
    (1,1),
    (0,1),
    (-1,1),
    (-1,0),
    (-1,-1),
    (0, -1),
    (1,-1)
]

def print_map(map):
    for line in map:
        str_int = [str(item) for item in line]
        print(''.join(str_int))
    print('')
    print('')

for line in output:
    oct_line = []
    for octopus in line.strip():
        oct_line.append(int(octopus))
    map.append(oct_line)

flash_count = 0
for iteration in range(0, 100):
    flash = set()
    queue = []
    for y, oct_line in enumerate(map):
        for x, octopus in enumerate(oct_line):
            octopus += 1
            map[y][x] = octopus
            if octopus == 10:
                flash.add((y,x))
                queue.append((y,x))
                map[y][x] = 0
    for item in queue:
        for point in nearby:
            new_point = (item[0] + point[0], item[1] + point[1])
            if (new_point not in flash and new_point[0] >= 0 and new_point[0] < len(map) and
                new_point[1] >= 0 and new_point[1] < len(map[0])):
                # print(flash)
                map[new_point[0]][new_point[1]] += 1
                if map[new_point[0]][new_point[1]] == 10:
                    flash.add((new_point[0],new_point[1]))
                    queue.append((new_point[0],new_point[1]))
                    map[new_point[0]][new_point[1]] = 0
    print_map(map)
    flash_count += len(flash)
print(flash_count)