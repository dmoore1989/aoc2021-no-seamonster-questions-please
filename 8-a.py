f = open("8in.txt", "r")
output = f.readlines()
valid_len = set([2, 4, 3, 7])
count = 0
for code in output:
    numbers_on = code.strip().split(' | ')[1].split(' ')
    print(numbers_on)
    for number in numbers_on:
        if len(number) in valid_len:
            count += 1
print(count)
    
