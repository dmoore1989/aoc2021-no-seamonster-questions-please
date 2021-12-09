f = open("8in.txt", "r")
output = f.readlines()
num_map = {
    '0': 'abcefg',
    '1': 'cf',
    '2': 'acdeg',
    '3': 'acdfg',
    '4': 'bcdf',
    '5': 'abdfg',
    '6': 'abdefg',
    '7': 'acf',
    '8': 'abcdefg',
    '9': 'abcdfg'
}

def get_correct_mapping(mapping):
    letters = set('abcdefg')
    used = set()
    test_perm = {}
    return iterate_pastability(mapping, letters, test_perm, used, 0, 0)

def iterate_pastability(mapping, letters, test_perm, used, char, answer):
    string = 'abcdefg'
    if len(letters) > 0:
        for letter in letters:
            test_perm[string[char]] = letter
            used.add(letter)
            new_letters = letters - set(letter)
            answer = iterate_pastability(mapping, new_letters, test_perm, used, char + 1, answer)
            if answer:
                return answer
    else:
        translation = {}
        for num, string in num_map.items():
            translated_string = ''
            for char in string:
                translated_string += test_perm[char]
            translation[''.join(sorted(translated_string))] = num
        if set(key for key in translation.keys()) == mapping:
            return translation
        else:
            return False
sum = 0  
for code in output:
    numbers_on = code.strip().split(' | ')
    mapping = set()
    for number in numbers_on[0].split(' '):
        # print(number)
        mapping.add(''.join(sorted(number)))
    letters = set('abcdefg')
    test_perm = {}
    mapping = get_correct_mapping(mapping)
    numstring = ''
    for digit in numbers_on[1].split():
        numstring += mapping[''.join(sorted(digit))]
    sum += int(numstring)
print(sum)
        
                

    
