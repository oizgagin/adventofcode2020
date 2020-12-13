def solution(actions):
    d = {'x': 10, 'y': 1}

    def rotate_left():
        d['x'], d['y'] = -d['y'], d['x']

    def rotate(degrees, direction):
        if direction == 'R':
            degrees = 360 - degrees
        for i in range(degrees // 90):
            rotate_left()

    x, y = 0, 0
    for action in actions:
        if action[0] == 'N':
            d['y'] += action[1]
        if action[0] == 'S':
            d['y'] -= action[1]
        if action[0] == 'E':
            d['x'] += action[1]
        if action[0] == 'W':
            d['x'] -= action[1]

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
