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
memo = {}
for case in range(min, max + 1):
    fuel = 0
    for number in numbers:
        fuel_base = abs(case - number)
        total_fuel = 0 
        if fuel_base in memo:
            total_fuel = memo[fuel_base]
        else:
            for base in range(1, fuel_base + 1):
                total_fuel += base
            memo[fuel_base] = total_fuel
        fuel += total_fuel
    if least_fuel is None or fuel < least_fuel:
        least_fuel = fuel
print(least_fuel) 

