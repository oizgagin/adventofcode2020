import string


def solution(lines):
    max = 0
    for line in lines:
        row = int(line[:7].translate(string.maketrans('FB', '01')), 2)
        col = int(line[7:].translate(string.maketrans('LR', '01')), 2)
        id = row * 8 + col
        if id > max:
            max = id
    return max


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
