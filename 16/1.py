def solution(conditions, tickets):

    def check_conds(val):
        for cond in conditions.values():
            if any(c[0] <= val <= c[1] for c in cond):
                return True
        return False

    def get_invalid_values(ticket):
        return filter(lambda val: not check_conds(val), ticket)

    acc = 0
    for ticket in tickets:
        for val in get_invalid_values(ticket):
            acc += val
    return acc


def parse(input):
    conditions, tickets = input.split('\n\n')[0].splitlines(), input.split('\n\n')[2].splitlines()[1:]

    conds = {}
    for cond in conditions:
        name = cond.split(":")[0]
        ranges = map(lambda s: (int(s.split('-')[0]), int(s.split('-')[1])), cond.split(':')[1].split(' or '))
        conds[name] = ranges

    return conds, map(lambda s: map(int, s.split(',')), tickets)


def main():
    input = open("input", "r").read()
    print solution(*parse(input))


main()
