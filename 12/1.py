def solution(actions):
    d = {'x': 1, 'y': 0}

    def rotate_left():
        if (d['x'], d['y']) == (-1, 0):
            d['x'], d['y'] = 0, -1
        elif (d['x'], d['y']) == (0, -1):
            d['x'], d['y'] = 1, 0
        elif (d['x'], d['y']) == (1, 0):
            d['x'], d['y'] = 0, 1
        elif (d['x'], d['y']) == (0, 1):
            d['x'], d['y'] = -1, 0

    def rotate(degrees, direction):
        if direction == 'R':
            degrees = 360 - degrees
        for i in range(degrees // 90):
            rotate_left()

    x, y = 0, 0
    for action in actions:
        if action[0] == 'N':
            y += action[1]

        if action[0] == 'S':
            y -= action[1]

        if action[0] == 'E':
            x += action[1]

        if action[0] == 'W':
            x -= action[1]

        if action[0] == 'F':
            x += d['x'] * action[1]
            y += d['y'] * action[1]

        if action[0] == 'L':
            rotate(action[1], 'L')

        if action[0] == 'R':
            rotate(action[1], 'R')

    return abs(x) + abs(y)


def parse(input):
    return map(lambda l: (l[0], int(l[1:])), input.splitlines())


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
