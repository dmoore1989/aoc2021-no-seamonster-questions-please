f = open("7in.txt", "r")
output = f.readline().split(',')
numbers = []
min = None
max = None
for item in output:
    number = int(item)
    numbers.append(number)
    if min is None or number < min:
        min = number
    if max is None or number > max:
        max = number

least_fuel = None
for case in range(min, max + 1):
    fuel = 0
    for number in numbers:
        fuel += abs(case - number)
    if least_fuel is None or fuel < least_fuel:
        least_fuel = fuel
print(least_fuel) 

