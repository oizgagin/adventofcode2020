def slopes(lines, dx, dy):
    trees = 0

    x, y = 0, 0
    while y < len(lines):
        if lines[y][x] == '#':
            trees += 1

        x, y = (x + dx) % len(lines[0]), y + dy

    return trees


def solution(lines):
    return slopes(lines, 3, 1)


def parse(lines):
    return lines


def main():
    lines = map(str.strip, open("input", "r").readlines())
    print solution(parse(lines))


main()
