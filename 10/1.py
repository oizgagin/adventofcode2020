def solution(jolts):
    jolts = [0] + jolts + [max(jolts)+3]
    jolts.sort()

    d1, d3 = 0, 0
    for i in xrange(1, len(jolts)):
        d = jolts[i] - jolts[i-1]
        if d == 1:
            d1 += 1
        if d == 3:
            d3 += 1

    return d1 * d3


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
