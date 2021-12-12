# import sys

# class DevNull:
#     def write(self, msg):
#         pass

# sys.stderr = DevNull()

f = open("12in.txt", "r")
output = f.readlines()

def explore_cave(cave_paths, cave, visited_smol_caves):
    count = 0
    if cave in visited_smol_caves:
        return 0
    if cave == 'start':
        return 0
    if cave == 'end':
        return 1
    if cave == cave.lower():
        visited_smol_caves.add(cave)
    for new_cave in cave_paths[cave]:
        count += explore_cave(cave_paths, new_cave, visited_smol_caves.copy())
    return count
    

cave_paths = {}
for line in output:
    caves = line.strip().split('-')
    if caves[0] not in cave_paths:
        cave_paths[caves[0]] = []
    if caves[1] not in cave_paths:
        cave_paths[caves[1]] = [] 
    cave_paths[caves[0]].append(caves[1])
    cave_paths[caves[1]].append(caves[0])
count_of_caves = 0
del cave_paths['end']
for cave in cave_paths['start']:
    visited_smol_caves = set()
    count_of_caves += explore_cave(cave_paths, cave, visited_smol_caves)
print(count_of_caves)