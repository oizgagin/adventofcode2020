def solution(grid):
    def is_occupied(row, col):
        return grid[row][col] == '#'

    def occupy(row, col):
        grid[row][col] = '#'

    def is_empty(row, col):
        return grid[row][col] == 'L'

    def empty(row, col):
        grid[row][col] = 'L'

    def is_floor(row, col):
        return grid[row][col] == '.'

    def sum(c1, c2):
        return (c1[0] + c2[0], c1[1] + c2[1])

    def get_nbrs(row, col):
        coords = []

        coord = (row, col)
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue

                d = (dr, dc)
                c = coord

                while True:
                    c = sum(c, d)
                    if not (0 <= c[0] < len(grid) and 0 <= c[1] < len(grid[0])):
                        break

                    if is_floor(*c):
                        continue

                    coords.append(c)
                    break

        return coords

    def get_occupied_nbrs(row, col):
        return len(filter(lambda coord: is_occupied(*coord), get_nbrs(row, col)))

    def get_empty_nbrs(row, col):
        return len(filter(lambda coord: is_empty(*coord), get_nbrs(row, col)))

    def count_occupied():
        return len(filter(lambda coord: is_occupied(*coord), [
            (row, col) for row in xrange(len(grid)) for col in xrange(len(grid[0]))
        ]))

    while True:
        to_occupy, to_empty = [], []

        for row in xrange(len(grid)):
            for col in xrange(len(grid[0])):
                if is_empty(row, col) and get_occupied_nbrs(row, col) == 0:
                    to_occupy.append((row, col))
                if is_occupied(row, col) and get_occupied_nbrs(row, col) >= 5:
                    to_empty.append((row, col))

        if len(to_occupy) == 0 and len(to_empty) == 0:
            return count_occupied()

        for coord in to_occupy:
            occupy(*coord)

        for coord in to_empty:
            empty(*coord)


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
