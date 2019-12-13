def calculate_fuel_required(mass):
    return int(mass / 3) - 2

def calculate_fuel_for_module(module_mass):
    total = 0
    fuel_required_for_fuel = calculate_fuel_required(module_mass)
    while fuel_required_for_fuel > 0:
        total += fuel_required_for_fuel
        fuel_required_for_fuel = calculate_fuel_required(fuel_required_for_fuel)

    return total

with open('input.txt') as input:
    masses = [int(line) for line in input.readlines()]
    fuel_for_each_module = [calculate_fuel_for_module(mass) for mass in masses]
    total_fuel_required = sum(fuel_for_each_module)
    print(total_fuel_required)