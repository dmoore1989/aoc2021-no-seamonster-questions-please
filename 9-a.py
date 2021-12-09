f = open("9in.txt", "r")
output = f.readlines()
map = []
pastabilities = [
    (1,0),
    (-1,0),
    (0,-1),
    (0,1)
]
total =0
for line in output:
    line = line.strip()
    mapline = []
    for amount in line:
        mapline.append(int(amount))
    map.append(mapline)
for y, mapline in enumerate(map):
    for x, point in enumerate(mapline):
        count = 0
        for pastability in pastabilities:
            if (x + pastability[1] < 0 or x + pastability[1] >= len(mapline)
                or y + pastability[0] < 0 or y + pastability[0] >= len(map)
                or map[y + pastability[0]][x + pastability[1]] > point):
                    count += 1
        if count == 4:
            total += point + 1
print(total)
    
