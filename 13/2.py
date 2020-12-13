import fractions


def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return x0, y0


def solve(a1, n1, a2, n2):
    m1, m2 = xgcd(n1, n2)

    sol = a1 * m2 * n2 + a2 * m1 * n1
    if sol < 0:
        sol %= n1 * n2
    return sol


def solution(ts, notes):
    ids = map(lambda t: (t[1] - t[0], t[1]), filter(lambda t: t[1] != 'x', enumerate(notes)))

    a1, n1, a2, n2 = ids[0][0], ids[0][1], ids[1][0], ids[1][1]
    sol = solve(a1, n1, a2, n2)

    for i in xrange(2, len(ids)):
        a1, n1 = sol, n1 * n2
        a2, n2 = ids[i][0], ids[i][1]
        sol = solve(a1, n1, a2, n2)

    mul = reduce(lambda acc, x: acc * x, map(lambda t: t[1], ids), 1)
    return sol % mul


def parse(input):
    lines = input.splitlines()
    ts = int(lines[0])
    notes = map(lambda c: c if c == 'x' else int(c), lines[1].split(','))
    return ts, notes


def main():
    input = open("input", "r").read()
    print solution(*parse(input))


main()
