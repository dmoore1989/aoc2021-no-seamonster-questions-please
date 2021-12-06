f = open("6in.txt", "r")
output = f.readline().split(',')
fishes = []
for item in output:
    fishes.append(int(item))

def number_of_fish_birthed(days_to_birth, total_days, memo):
    if days_to_birth == 8 and total_days in memo:
        return [memo[total_days], memo]
    count = 1
    for day in range(total_days, 0, -1):
        if days_to_birth >= 1:
            days_to_birth -= 1
        else:
            days_to_birth = 6
            new_fish, memo = number_of_fish_birthed(8, day - 1, memo)
            count += new_fish
    memo[total_days] = count
    return [count, memo]

count = 0
memo = {}
for fish in fishes:
    number, memo = number_of_fish_birthed(fish, 256, memo)
    # print(memo)
    count += number
print(count)
        

            