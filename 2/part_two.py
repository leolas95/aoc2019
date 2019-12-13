# para V(noun, verb) | 0 <= noun, verb <= 99
# hallar el par (noun, verb) | intcode[0] == 19690720

import part_one

intcode = [int(x) for x in open('input.txt').readline().split(',')]

for noun in range(0, 100):
    for verb in range(0, 100):
        intcode_copy = intcode.copy()
        intcode_copy[1] = noun
        intcode_copy[2] = verb
        result = part_one.run_program(intcode_copy)
        if result == 19690720:
            print(100 * noun + verb)
            exit(0)
