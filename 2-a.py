f = open("2in.txt", "r")
instructions = f.readlines()
position= 0
depth= 0
for instruction in instructions:
    instruction_li = instruction.split(' ')
    if instruction_li[0] == 'forward':
        position += int(instruction_li[1])
    elif instruction_li[0] == 'down':
        depth += int(instruction_li[1])
    elif instruction_li[0] == 'up':
        depth -= int(instruction_li[1])
print(position * depth)