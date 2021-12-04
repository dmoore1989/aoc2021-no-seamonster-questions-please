f = open("3in.txt", "r")
ox_output = f.readlines()
co_output = ox_output[:]

def trim_failing_numbers(array, position, num):
    new_arr = []
    for item in array:
        if item[position] == num:
            new_arr.append(item)
    return new_arr
    

for position in range(0, len(ox_output[0])- 1):
    if len(co_output) == 1:
        break
    zeroes = 0
    ones = 0
    
    for log in ox_output:
        if log[position] == '0':
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        num = '0'
    else:
        num = '1'
    ox_output = trim_failing_numbers(ox_output, position, num)


for position in range(0, len(co_output[0])- 1):
    if len(co_output) == 1:
        break 
    zeroes = 0
    ones = 0
    for log in co_output:
        if log[position] == '0':
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        num = '1'
    else:
        num = '0'
    co_output = trim_failing_numbers(co_output, position, num)
print(ox_output, co_output)
        
print(int(ox_output[0], 2) * int(co_output[0], 2))