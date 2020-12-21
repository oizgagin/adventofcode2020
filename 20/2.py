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

    rotated_tiles = {}

    rotated = {}
    for id, tile in tiles.iteritems():
        for i in xrange(0, 4):
            rotated['%s_0_%s' % (id, i)] = get_borders(tile)
            rotated_tiles['%s_0_%s' % (id, i)]  = tile

            tile = rotate_right(tile)

        tile = flip_horizontally(rotate_right(tile))

        for i in xrange(0, 4):
            rotated['%s_1_%s' % (id, i)] = get_borders(tile)
            rotated_tiles['%s_1_%s' % (id, i)]  = tile
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

    N = int(math.sqrt(len(tiles)))

    table = [None] * N
    for i in xrange(N):
        table[i] = [None] * N

    for id, nbrs in graph.iteritems():
        if len(nbrs['left']) == 0 and len(nbrs['right']) == 1 and len(nbrs['up']) == 0 and len(nbrs['down']) == 1:
            table[0][0] = id
            break

    for i in xrange(1, N):
        table[0][i] = graph[table[0][i-1]]['right'][0]

    for j in xrange(1, N):
        table[j][0] = graph[table[j-1][0]]['down'][0]

    for i in xrange(1, N):
        for j in xrange(1, N):
            table[i][j] = graph[table[i-1][j]]['down'][0]

    def trim(tile):
        return [row[1:-1] for row in tile[1:-1]]

    def rows2str(tile):
        return [''.join(row) for row in tile]

    tiles = []
    for row in table:
        tiles.append([rotated_tiles[id] for id in row])

    pic = []
    for row in tiles:
        for i in xrange(8):
            pic.append(''.join(''.join(trim(tile)[i]) for tile in row))

    def monster_coords(i, j):
        return [
            (i-1, j+18),
            (i, j), (i, j+5), (i, j+6), (i, j+11), (i, j+12), (i, j+17), (i, j+18), (i, j+19),
            (i+1, j+1), (i+1, j+4), (i+1, j+7), (i+1, j+10), (i+1, j+13), (i+1, j+16),
        ]

    def count_monsters(pic):
        res = 0
        for i in xrange(1, len(pic)-1):
            for j in xrange(0, len(pic[0])-20):
                try:
                    if all(
                        pic[coord[0]][coord[1]] == '#'
                        for coord in monster_coords(i, j)
                    ):
                        res += 1
                except:
                    pass
        return res

    def count_pixels(pic):
        return sum(row.count('#') for row in pic)

    for i in xrange(0, 4):
        monsters = count_monsters(pic)
        if monsters != 0:
            return count_pixels(pic) - count_monsters(pic) * 15
        pic = rotate_right(pic)

    pic = rotate_right(pic)

    pic = flip_vertically(pic)

    for i in xrange(0, 4):
        monsters = count_monsters(pic)
        if monsters != 0:
            return count_pixels(pic) - count_monsters(pic) * 15
        pic = rotate_right(pic)


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
