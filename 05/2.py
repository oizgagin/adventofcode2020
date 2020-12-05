import string


def solution(lines):
    ids = []
    for line in lines:
        row = int(line[:7].translate(string.maketrans('FB', '01')), 2)
        col = int(line[7:].translate(string.maketrans('LR', '01')), 2)
        ids.append(row * 8 + col)

    ids.sort()

    for i in xrange(1, len(ids)-1):
        if ids[i+1] - ids[i] > 1:
            return (ids[i] + ids[i+1]) / 2


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
