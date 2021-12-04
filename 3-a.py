f = open("3in.txt", "r")
output = f.readlines()
gamma = ''
epsilon = ''
for position in range(0, len(output[0])- 1):
    zeroes = 0
    ones = 0
    for log in output:
        if log[position] == '0':
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
        
print(int(gamma, 2) * int(epsilon, 2))