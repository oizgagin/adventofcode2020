from collections import defaultdict

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

    def get_neighbours(c, r):
        return [move(c, r, d) for d in ('e', 'se', 'sw', 'w', 'nw', 'ne')]

    reversed_color = {
        'white': 'black',
        'black': 'white',
    }

    colors = defaultdict(lambda: 'white')

    minc, minr, maxc, maxr = 0, 0, 0, 0
    for dir in dirs:
        c, r = 0, 0
        for d in dir:
            c, r = move(c, r, d)

        colors[(c, r)] = reversed_color[colors[(c, r)]]

        minc = min(minc, c)
        minr = min(minr, r)
        maxc = max(maxc, c)
        maxr = max(maxr, r)

    for day in xrange(0, 100):
        minc, maxc = minc - 1, maxc + 1
        minr, maxr = minr - 1, maxr + 1

        to_black, to_white = [], []
        for c in xrange(minc, maxc+1):
            for r in xrange(minr, maxr+1):
                black_nbrs = 0
                for nbr in get_neighbours(c, r):
                    if colors[nbr] == 'black':
                        black_nbrs += 1

                if colors[(c, r)] == 'white' and black_nbrs == 2:
                    to_black.append((c, r))

                if colors[(c, r)] == 'black' and (black_nbrs == 0 or black_nbrs > 2):
                    to_white.append((c, r))

        for coord in to_black:
            colors[coord] = 'black'

        for coord in to_white:
            colors[coord] = 'white'

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
