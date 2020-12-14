def format_bin(n):
    return format(n, '#038b')[2:]


def apply_mask(n, mask):
    n = list(format_bin(n))

    for i, ch in enumerate(mask):
        if ch == '0':
            continue
        if ch == '1' or ch == 'X':
            n[i] = ch

    addrs = []

    def recurse(acc, i):
        if i == len(n):
            addrs.append(acc)
            return

        if n[i] in ('0', '1'):
            acc = (acc << 1) | (ord(n[i]) - ord('0'))
            recurse(acc, i+1)
            return

        recurse((acc << 1) | 1, i+1)
        recurse((acc << 1) | 0, i+1)

    recurse(0, 0)
    return addrs


def solution(program):
    mask = None

    mem = dict()

    for instr in program:

        if instr.startswith('mask'):
            mask = instr.split()[2]

        else:
            instr = instr[len('mem'):].split()
            addr, val = instr[0].strip('[]'), int(instr[2].strip())

            addrs = apply_mask(int(addr), mask)
            for addr in addrs:
                mem[addr] = val

    return sum(mem.values())


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
