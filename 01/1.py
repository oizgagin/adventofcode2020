def solution(ints):
    i, j = 0, len(ints)-1
    while i < j:
        s = ints[i] + ints[j]

        if s == 2020:
            return ints[i] * ints[j]

        if s < 2020:
            i += 1
        else:
            j -= 1


def main():
    ints = map(int, open("input", "r").readlines())
    ints.sort()

    print solution(ints)


main()
