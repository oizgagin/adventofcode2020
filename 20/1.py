import math


def solution(tiles):

    def list2int(l):
        return int(''.join(l).replace('.', '0').replace('#', '1'), 2)

    def get_borders(tile):
        return {
            'up': list2int(tile[0]),
            'down': list2int(tile[-1]),
            'left': list2int(map(lambda l: l[0], tile)),
            'right': list2int(map(lambda l: l[-1], tile)),
        }

    def rotate_right(tile):
        return [
            [row[col] for row in reversed(tile)]
            for col in xrange(len(tile[0]))
        ]

    def flip_vertically(tile):
        return list(reversed(tile))

    def flip_horizontally(tile):
        return [list(reversed(row)) for row in tile]

    rotated = {}
    for id, tile in tiles.iteritems():
        for i in xrange(0, 4):
            rotated['%s_0_%s' % (id, i)] = get_borders(tile)
            tile = rotate_right(tile)

        tile = flip_horizontally(rotate_right(tile))

        for i in xrange(0, 4):
            rotated['%s_1_%s' % (id, i)] = get_borders(tile)
            tile = rotate_right(tile)

    graph = {}
    for id, tile in rotated.iteritems():
        graph[id] = {'up': [], 'down': [], 'left': [], 'right': []}

        for subid, subtile in rotated.iteritems():
            if id.split('_')[0] == subid.split('_')[0]:
                continue

            if tile['up'] == subtile['down']:
                graph[id]['up'].append(subid)

            if tile['down'] == subtile['up']:
                graph[id]['down'].append(subid)

            if tile['left'] == subtile['right']:
                graph[id]['left'].append(subid)

            if tile['right'] == subtile['left']:
                graph[id]['right'].append(subid)

    ids = set()

    for id, nbrs in graph.iteritems():
        if len(nbrs['left']) == 0 and len(nbrs['right']) == 1 and len(nbrs['up']) == 0 and len(nbrs['down']) == 1:
            ids.add(int(id.split('_')[0]))

    return reduce(lambda acc, x: acc * x, ids, 1)


def parse(input):
    tiles = {}
    for block in input.split("\n\n"):
        id = block.splitlines()[0].split()[1].strip(":")
        tiles[id] = map(list, block.splitlines()[1:])
    return tiles


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
