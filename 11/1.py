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

    def get_nbrs(row, col):
        coords = [(row + dr, col + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1)]
        coords = filter(lambda coord: 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]), coords)
        coords = filter(lambda coord: coord != (row, col) and not is_floor(*coord), coords)
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
                if is_occupied(row, col) and get_occupied_nbrs(row, col) >= 4:
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
