from collections import defaultdict


def solution(grid):

    def get_neighbours(x, y, z, w):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    for dw in (-1, 0, 1):
                        if not (dx == 0 and dy == 0 and dz == 0 and dw == 0):
                            yield (x + dx, y + dy, z + dz, w + dw)

    def is_active(x, y, z, w):
        return grid[x][y][z][w] == '#'

    def get_active_neighbours_count(x, y, z, w):
        active = 0
        for nx, ny, nz, nw in get_neighbours(x, y, z, w):
            if is_active(nx, ny, nz, nw):
                active += 1
        return active

    def activate(x, y, z, w):
        grid[x][y][z][w] = '#'

    def inactivate(x, y, z, w):
        grid[x][y][z][w] = '.'

    minx, maxx = 0, len(grid)-1
    miny, maxy = 0, len(grid[0])-1
    minz, maxz = 0, 0
    minw, maxw = 0, 0

    for i in xrange(6):
        minx, maxx = minx - 1, maxx + 1
        miny, maxy = miny - 1, maxy + 1
        minz, maxz = minz - 1, maxz + 1
        minw, maxw = minw - 1, maxw + 1

        to_activate, to_inactivate = [], []

        for x in xrange(minx, maxx+1):
            for y in xrange(miny, maxy+1):
                for z in xrange(minz, maxz+1):
                    for w in xrange(minw, maxw+1):
                        active = get_active_neighbours_count(x, y, z, w)

                        if is_active(x, y, z, w) and active not in (2, 3):
                            to_inactivate.append((x, y, z, w))

                        if not is_active(x, y, z, w) and active == 3:
                            to_activate.append((x, y, z, w))

        for t in to_activate:
            activate(*t)

        for t in to_inactivate:
            inactivate(*t)

    active = 0
    for x in xrange(minx, maxx+1):
        for y in xrange(miny, maxy+1):
            for z in xrange(minz, maxz+1):
                for w in xrange(minw, maxw+1):
                    if is_active(x, y, z, w):
                        active += 1
    return active


def parse(input):
    sp = input.splitlines()

    grid = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.')))))
    for y, xs in enumerate(sp):
        for x, v in enumerate(xs):
            grid[x][y][0][0] = v
    return grid


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
