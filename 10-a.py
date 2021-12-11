f = open("10in.txt", "r")
output = f.readlines()
closing_characters = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}
scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points = 0
for line in output:
    line = line.strip()
    stack = []
    for char in line:
        if char in closing_characters:
            if closing_characters[char] != stack.pop():
                points += scores[char]
                break
        else:
            stack.append(char)
            
print(points)
