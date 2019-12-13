total_fuel_required = 0
with open('input.txt') as input:
    for line in input.readlines():
        # The int() function already rounds down floating point numbers
        fuel_required = int((int(line) / 3)) - 2
        total_fuel_required += fuel_required

print(total_fuel_required)