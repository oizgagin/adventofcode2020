from collections import defaultdict


def solution(conditions, ticket, tickets):

    def check_conds(val):
        for cond in conditions.values():
            if any(c[0] <= val <= c[1] for c in cond):
                return True
        return False

    def is_valid_ticket(ticket):
        return len(filter(lambda val: not check_conds(val), ticket)) == 0

    tickets = filter(is_valid_ticket, tickets)

    candidates = defaultdict(list)
    for name, conds in conditions.iteritems():
        for i in xrange(len(ticket)):
            if all(
                any(c[0] <= val <= c[1] for c in conds)
                for val in map(lambda t: t[i], tickets)
            ):
                candidates[name].append(i)

    determined = dict()
    while True:
        dname, dno = None, None

        for name, possibles in candidates.iteritems():
            if len(possibles) == 1:
                dname, dno = name, possibles[0]
                break

        determined[dname] = dno

        for name, possibles in candidates.iteritems():
            if dno in possibles:
                possibles.remove(dno)

        if len(determined) == len(candidates):
            break

    res = 1
    for fname, fno in determined.iteritems():
        if fname.startswith("departure"):
            res *= ticket[fno]
    return res


def parse(input):
    split = input.split('\n\n')
    conditions, ticket, tickets = split[0].splitlines(), split[1].splitlines()[1], split[2].splitlines()[1:]

    conds = {}
    for cond in conditions:
        name = cond.split(":")[0]
        ranges = map(lambda s: (int(s.split('-')[0]), int(s.split('-')[1])), cond.split(':')[1].split(' or '))
        conds[name] = ranges

    return conds, map(int, ticket.split(',')), map(lambda s: map(int, s.split(',')), tickets)


def main():
    input = open("input", "r").read()
    print solution(*parse(input))


main()
