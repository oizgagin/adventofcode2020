def solution(cups):
    curr_val = cups[0]

    for _ in xrange(100):
        curr_idx = cups.index(curr_val)
        taken = [
            cups[(curr_idx + 1) % len(cups)],
            cups[(curr_idx + 2) % len(cups)],
            cups[(curr_idx + 3) % len(cups)],
        ]

        for cup in taken:
            cups.remove(cup)

        dest_val = curr_val - 1
        while dest_val >= 1 and dest_val in taken:
            dest_val -= 1

        if dest_val == 0:
            dest_val = max(cups)

        dest_idx = cups.index(dest_val)
        cups = cups[:(dest_idx + 1) % len(cups)] + taken + cups[(dest_idx + 1) % len(cups):]

        curr_val = cups[(cups.index(curr_val) + 1) % len(cups)]

    one_idx = cups.index(1)
    s = ''
    for i in xrange(len(cups)-1):
        s += str(cups[(one_idx + 1 + i) % len(cups)])
    return s


def parse(input):
    return map(int, list(input.strip()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
