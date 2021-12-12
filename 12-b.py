# import sys

# class DevNull:
#     def write(self, msg):
#         pass

# sys.stderr = DevNull()

f = open("12in.txt", "r")
output = f.readlines()

def explore_cave(cave_paths, cave, visited_smol_caves, smol_cave_2, arr, cave_set):
    count = 0
    if cave in visited_smol_caves:
        return None
    if cave == 'start':
        return None
    if cave == 'end':
        cave_set.add('-'.join((arr + ['end'])))
        return
        
    new_visited_smol_caves = visited_smol_caves.copy()
    if cave == cave.lower():
        new_visited_smol_caves.add(cave)
    for new_cave in cave_paths[cave]:
        explore_cave(cave_paths, new_cave, new_visited_smol_caves.copy(), smol_cave_2, arr + [cave], cave_set)
        if smol_cave_2 is None and cave == cave.lower():
            explore_cave(cave_paths, new_cave, visited_smol_caves.copy(), cave, arr + [cave],cave_set)

cave_paths = {}
for line in output:
    caves = line.strip().split('-')
    if caves[0] not in cave_paths:
        cave_paths[caves[0]] = []
    if caves[1] not in cave_paths:
        cave_paths[caves[1]] = [] 
    cave_paths[caves[0]].append(caves[1])
    cave_paths[caves[1]].append(caves[0])
cave_perms = set()
del cave_paths['end']
for cave in cave_paths['start']:
    visited_smol_caves = set()
    explore_cave(cave_paths, cave, visited_smol_caves, None, ['start'], cave_perms)
print(len(cave_perms))