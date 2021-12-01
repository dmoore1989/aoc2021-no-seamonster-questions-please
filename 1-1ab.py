f = open("1in.txt", "r")
depths= f.readlines()
count_1 = 0
count_3 = 0
for i in range(1, len(depths)):
    depth1= int(depths[i])
    depth2=  int(depths[i - 1])
    if depth1 > depth2:
        count_1 += 1
    final_item = depths[i]
print(count_1)

for i in range(3, len(depths)):
    depth1= int(depths[i]) + int(depths[i - 1]) + int(depths[i -2])
    depth2=  int(depths[i - 1]) + int(depths[i - 2]) + int(depths[i - 3])
    if depth1 > depth2:
        count_3 += 1
    final_item = depths[i]
print(count_3)
