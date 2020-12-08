def solution(program):
    addr = 0
    acc = 0

    executed = set()
    while True:
        if addr in executed:
            return acc

        executed.add(addr)

        instr = program[addr]

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


def parse(input):
    return map(lambda l: (l[0], int(l[1])), map(str.split, input.splitlines()))


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
