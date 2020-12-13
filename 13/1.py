def solution(ts, notes):
    ids = filter(lambda note: note != 'x', notes)

    min, min_id = None, None
    for id in ids:
        t = ts + (id - ts % id)
        if min is None or t < min:
            min, min_id = t, id

    return (min - ts) * min_id


def parse(input):
    lines = input.splitlines()
    ts = int(lines[0])
    notes = map(lambda c: c if c == 'x' else int(c), lines[1].split(','))
    return ts, notes


def main():
    input = open("input", "r").read()
    print solution(*parse(input))


main()
