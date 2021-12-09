f = open("9in.txt", "r")
output = f.readlines()
map = []
pastabilities = [
    (1,0),
    (-1,0),
    (0,-1),
    (0,1)
]
def visit_basins(map, position, total, visited):
    if position in visited:
        return total, visited
    y = position[0]
    x = position[1]
    visited.add(position)
    if map[y][x] == 9:
        return total, visited
    total += 1
    for pastability in pastabilities:
        if (x + pastability[1] >= 0 and x + pastability[1] < len(map[y])
            and y + pastability[0] >= 0 and y + pastability[0] < len(map)):
            new_pos = (y + pastability[0], x + pastability[1])
            total, visited = visit_basins(map, new_pos, total, visited)
    return total, visited
    
                
            
visited = set()
basins = []
for line in output:
    line = line.strip()
    mapline = []
    for amount in line:
        mapline.append(int(amount))
    map.append(mapline)
for y, mapline in enumerate(map):
    for x, point in enumerate(mapline):
        total = 0
        total, visited = visit_basins(map, (y,x), total, visited)
        basins.append(total)
sort_basin = sorted(basins, reverse=True)
print(sort_basin[0] * sort_basin[1] * sort_basin[2])
    
