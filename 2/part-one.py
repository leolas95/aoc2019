import fileinput


def fetch(intcode, pc):
    return intcode[pc]


# Returns a tuple containing the operands, operator and fn to apply
def decode(opcode, intcode, pc):
    op1 = intcode[intcode[pc+1]]
    op2 = intcode[intcode[pc+2]]
    position = intcode[pc+3]

    if opcode == 1:
        return (op1, op2, position, int.__add__)
    elif opcode == 2:
        return (op1, op2, position, int.__mul__)


def execute(op1, op2, position, fn, intcode):
    intcode[position] = fn.__call__(op1, op2)


pc = 0
intcode = [int(x) for x in open('input.txt').readline().split(',')]
intcode[1] = 12
intcode[2] = 2

opcode = fetch(intcode, pc)
while opcode != 99:
    operation_args = decode(opcode, intcode, pc)
    execute(*operation_args, intcode)
    pc += 4
    opcode = fetch(intcode, pc)

print(intcode[0])
