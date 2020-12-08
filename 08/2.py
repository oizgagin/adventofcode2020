def execute(program):
    addr = 0
    acc = 0

    seen = set()
    while addr < len(program):
        instr = program[addr]

        if addr in seen:
            return None

        seen.add(addr)

        if instr[0] == 'nop':
            addr += 1
            continue

        if instr[0] == 'acc':
            acc += instr[1]
            addr += 1
            continue

        if instr[0] == 'jmp':
            addr += instr[1]
            continue

    return acc


def solution(program):
    reverse = {'nop': 'jmp', 'jmp': 'nop'}

    for i in xrange(0, len(program)):
        if program[i][0] in ('nop', 'jmp'):
            program[i] = (reverse[program[i][0]], program[i][1])
            res = execute(program)
            if res is not None:
                return res
            program[i] = (reverse[program[i][0]], program[i][1])


def parse(input):
    return map(lambda l: (l[0], int(l[1])), map(str.split, input.splitlines()))


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
