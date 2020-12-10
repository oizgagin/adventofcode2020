from collections import defaultdict


def solution(jolts):
    jolts = [0] + jolts + [max(jolts)+3]
    jolts.sort()

    choices = {}
    for jolt in reversed(jolts):
        ch1 = choices[jolt+1] if (jolt+1) in choices else 0
        ch2 = choices[jolt+2] if (jolt+2) in choices else 0
        ch3 = choices[jolt+3] if (jolt+3) in choices else 0
        choices[jolt] = (ch1 + ch2 + ch3) or 1

    return choices[0]


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print solution(parse(input))


main()
