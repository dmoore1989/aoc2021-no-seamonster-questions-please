f = open("13in.txt", "r")
output = f.readlines()
folds = {
    'x':0,
    'y':1
}
instructions = []
coordinates = set()
for line in output:
    line = line.strip()
    if len(line) > 0:
        if line[0:10] == 'fold along':
            instructions.append((line[11:12], int(line[13:])))
        else:
            coordinate = line.split(',')
            coordinates.add((int(coordinate[0]), int(coordinate[1])))
instruction = instructions[0]
fold = folds[instruction[0]]
for coordinate in coordinates.copy():
    if coordinate[fold] > instruction[1]:
        coordinates.remove(coordinate)
        if fold == 0:
            new_coordinate = (2 * instruction[1] - coordinate[fold], coordinate[1])
        else:
            new_coordinate = (coordinate[0], 2 * instruction[1] - coordinate[fold])
        coordinates.add(new_coordinate)

print(len(coordinates))