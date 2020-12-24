def solution(dirs):

    def move(c, r, d):
        if d == 'e':
            return c + 1, r
        if d == 'w':
            return c - 1, r
        if d == 'se':
            r -= 1
            if r % 2 == 0:
                c += 1
            return c, r
        if d == 'sw':
            r -= 1
            if r % 2 != 0:
                c -= 1
            return c, r
        if d == 'ne':
            r += 1
            if r % 2 == 0:
                c += 1
            return c, r
        if d == 'nw':
            r += 1
            if r % 2 != 0:
                c -= 1
            return c, r

    reversed_color = {
        'white': 'black',
        'black': 'white',
    }

    colors = {}

    for dir in dirs:
        c, r = 0, 0
        for d in dir:
            c, r = move(c, r, d)

        if (c, r) not in colors:
            colors[(c, r)] = 'black'
        else:
            colors[(c, r)] = reversed_color[colors[(c, r)]]

    blacks = 0
    for _, color in colors.iteritems():
        if color == 'black':
            blacks += 1
    return blacks


def parse(input):
    dirs = []
    for line in input.splitlines():
        dir = []
        while line:
            for direction in ['e', 'se', 'sw', 'w', 'nw', 'ne']:
                if line.startswith(direction):
                    dir.append(direction)
                    line = line[len(direction):]
                    break
        dirs.append(dir)
    return dirs


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
