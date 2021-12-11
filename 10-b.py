f = open("10in.txt", "r")
output = f.readlines()
closing_characters = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}
scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}
points = []
for line in output:
    line = line.strip()
    stack = []
    corrupt = False
    for char in line:
        if char in closing_characters:
            if closing_characters[char] != stack.pop():
                corrupt = True
                break
        else:
            stack.append(char)
    if not corrupt:
        count = 0
        for item in stack[::-1]:
            count = (count * 5) + scores[item]
        points.append(count)
    
print(sorted(points)[len(points)/2])