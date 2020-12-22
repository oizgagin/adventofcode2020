from collections import deque


def score(deck):
    mul = len(deck)

    sum = 0
    for v in deck:
        sum += v * mul
        mul -= 1
    return sum


def solution(decks):
    d1, d2 = decks[0], decks[1]

    while True:
        if len(d1) == 0 or len(d2) == 0:
            break

        v1, v2 = d1.popleft(), d2.popleft()

        if v1 > v2:
            d1.append(v1)
            d1.append(v2)
        else:
            d2.append(v2)
            d2.append(v1)

    if len(d1) != 0:
        return score(d1)

    return score(d2)


def parse(input):
    decks = []
    for raw_deck in input.split("\n\n"):
        decks.append(deque(map(int, raw_deck.splitlines()[1:])))
    return decks


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
