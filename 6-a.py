f = open("6in.txt", "r")
output = f.readline().split(',')
fishes = []
for item in output:
    fishes.append(int(item))
for day in range(0, 256):
    new_fishes = []
    for idx, fish in enumerate(fishes):
        if fish >= 1:
            fishes[idx] -= 1
        else:
            fishes[idx] = 6
            new_fishes.append(8)
    fishes = fishes + new_fishes
print(len(fishes))