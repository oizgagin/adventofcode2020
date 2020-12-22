from collections import deque


def score(deck):
    mul = len(deck)

    sum = 0
    for v in deck:
        sum += v * mul
        mul -= 1
    return sum


def play_game(d1, d2):
    seen = set()

    while True:
        if '%s' % d1 in seen or '%s' % d2 in seen:
            return 1, -1

        seen.add('%s' % d1)
        seen.add('%s' % d2)

        if len(d1) == 0:
            return 2, score(d2)

        if len(d2) == 0:
            return 1, score(d1)

        v1, v2 = d1.popleft(), d2.popleft()
        if not (v1 <= len(d1) and v2 <= len(d2)):
            if v1 > v2:
                d1.append(v1)
                d1.append(v2)
            else:
                d2.append(v2)
                d2.append(v1)
        else:
            winner, _ = play_game(deque(list(d1)[:v1]), deque(list(d2)[:v2]))
            if winner == 1:
                d1.append(v1)
                d1.append(v2)
            else:
                d2.append(v2)
                d2.append(v1)


def solution(decks):
    _, s = play_game(decks[0], decks[1])
    return s


def parse(input):
    decks = []
    for raw_deck in input.split("\n\n"):
        decks.append(deque(map(int, raw_deck.splitlines()[1:])))
    return decks


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
