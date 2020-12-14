def format_bin(n):
    return format(n, '#038b')[2:]


def apply_mask(n, mask):
    n = list(format_bin(n))
    for i, ch in enumerate(mask):
        if ch != 'X':
            n[i] = ch

    return int(''.join(n), 2)


def solution(program):
    mask = None

    mem = dict()

    for instr in program:

        if instr.startswith('mask'):
            mask = instr.split()[2]

        else:
            instr = instr[len('mem'):].split()
            addr, val = instr[0].strip(']'), int(instr[2].strip())

            mem[addr] = apply_mask(val, mask)

    return sum(mem.values())


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
